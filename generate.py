import yaml
from packaging import version
import argparse
from itertools import product
import os
import re

from mugibuilder import *

def to_qwt(qwt):
    if not qwt.startswith('qwt'):
        return 'qwt' + qwt
    return qwt

QWT_6_2_0 = "qwt6.2.0"
QWT_6_1_3 = "qwt6.1.3"
QWTS = [QWT_6_2_0, QWT_6_1_3]

def qwt_url(qwt):
    return {
        QWT_6_1_3: 'https://cfhcable.dl.sourceforge.net/project/qwt/qwt/6.1.3/qwt-6.1.3.zip',
        QWT_6_2_0: 'https://altushost-swe.dl.sourceforge.net/project/qwt/qwt/6.2.0/qwt-6.2.0.zip'
    }[qwt]

def qwt_local_path(qwt):
    return "C:\\Qwt-" + qwt.replace("qwt","")

def qwt_flavour_name(qwt, qt, compiler, arch):
    return "-".join([qwt, qt, compiler, arch])

def build_step(qwt, qt, compiler, arch, local):
    name = "flavour {} {} {} {}".format(qwt, qt, compiler, arch)
    c = Commander(name, qt, compiler, arch, local)
    c.aqt_install_qt()
    c.aqt_install_mingw()
    url = qwt_url(qwt)
    zip_name, qwt_dir_name = c.download(url)
    local_path = qwt_local_path(qwt)
    c.rmdir(qwt_dir_name)
    c.rmdir(local_path)
    c.extract(zip_name)
    c.call_vcvars()
    c.pushd(qwt_dir_name)
    c.qmake()
    c.make_install()
    c.popd()
    flavour_base = qwt_flavour_name(qwt, qt, compiler, arch)
    zip_name = flavour_base + ".zip"
    c.archive(zip_name, local_path)
    return c.pack()

def install_aqt_step(local):
    c = Commander("install aqtinstall", local=local)
    c.pip_install_aqtinstall()
    return c.pack()

def main():
    parser = argparse.ArgumentParser()
    add_spec_args(parser)
    parser.add_argument('--qwt', nargs='+', help="qwt versions to build")
    args = parser.parse_args()
    qts, compilers, archs = get_specs(args)
    if args.qwt is None:
        qwts = [QWT_6_2_0]
    else:
        qwts = args.qwt
    steps_local = []
    steps_github = []
    steps_local.append(install_aqt_step(local=True))
    steps_github.append(install_aqt_step(local=False))
    release_step = ReleaseStep()
    for qwt in qwts:
        qwt = to_qwt(qwt)
        if qwt not in QWTS:
            print("not implemented for qwt {}".format(qwt))
        for qt, compiler, arch in filter_specs(product(qts, compilers, archs)):
            steps_local.append(build_step(qwt, qt, compiler, arch, local=True))
            steps_github.append(build_step(qwt, qt, compiler, arch, local=False))
            flavour_base = qwt_flavour_name(qwt, qt, compiler, arch)
            zip_name = flavour_base + ".zip"
            release_step.add(zip_name)
    steps_github.append(release_step.github())
    base = os.path.dirname(__file__)
    workflow_path = os.path.join(base, ".github", "workflows", "main.yml")
    save_workflow(workflow_path, steps_github, on = ON_TAG, runs_on=WINDOWS_2019)
    batch_path = os.path.join(base, "main.bat")
    save_batch(batch_path, steps_local)

if __name__ == "__main__":
    main()
