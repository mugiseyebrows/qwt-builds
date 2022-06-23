import yaml
from packaging import version
import argparse
from itertools import product
import os
import re

QT_5_9_0 = "qt5.9.0"
QT_5_9_1 = "qt5.9.1"
QT_5_9_2 = "qt5.9.2"
QT_5_9_3 = "qt5.9.3"
QT_5_9_4 = "qt5.9.4"
QT_5_9_5 = "qt5.9.5"
QT_5_9_6 = "qt5.9.6"
QT_5_9_7 = "qt5.9.7"
QT_5_9_8 = "qt5.9.8"
QT_5_9_9 = "qt5.9.9"
QT_5_10_0 = "qt5.10.0"
QT_5_10_1 = "qt5.10.1"
QT_5_11_0 = "qt5.11.0"
QT_5_11_1 = "qt5.11.1"
QT_5_11_2 = "qt5.11.2"
QT_5_11_3 = "qt5.11.3"
QT_5_12_0 = "qt5.12.0"
QT_5_12_1 = "qt5.12.1"
QT_5_12_2 = "qt5.12.2"
QT_5_12_3 = "qt5.12.3"
QT_5_12_4 = "qt5.12.4"
QT_5_12_5 = "qt5.12.5"
QT_5_12_6 = "qt5.12.6"
QT_5_12_7 = "qt5.12.7"
QT_5_12_8 = "qt5.12.8"
QT_5_12_9 = "qt5.12.9"
QT_5_12_10 = "qt5.12.10"
QT_5_12_11 = "qt5.12.11"
QT_5_12_12 = "qt5.12.12"
QT_5_13_0 = "qt5.13.0"
QT_5_13_1 = "qt5.13.1"
QT_5_13_2 = "qt5.13.2"
QT_5_14_0 = "qt5.14.0"
QT_5_14_1 = "qt5.14.1"
QT_5_14_2 = "qt5.14.2"
QT_5_15_0 = "qt5.15.0"
QT_5_15_1 = "qt5.15.1"
QT_5_15_2 = "qt5.15.2"
QT_6_0_0 = "qt6.0.0"
QT_6_0_1 = "qt6.0.1"
QT_6_0_2 = "qt6.0.2"
QT_6_0_3 = "qt6.0.3"
QT_6_0_4 = "qt6.0.4"
QT_6_1_0 = "qt6.1.0"
QT_6_1_1 = "qt6.1.1"
QT_6_1_2 = "qt6.1.2"
QT_6_1_3 = "qt6.1.3"
QT_6_2_0 = "qt6.2.0"
QT_6_2_1 = "qt6.2.1"
QT_6_2_2 = "qt6.2.2"
QT_6_2_3 = "qt6.2.3"
QT_6_2_4 = "qt6.2.4"
QT_6_3_0 = "qt6.3.0"
QT_6_3_1 = "qt6.3.1"
QT_6_4_0 = "qt6.4.0"
QTS = [QT_5_9_0, QT_5_9_1, QT_5_9_2, QT_5_9_3, QT_5_9_4, QT_5_9_5, QT_5_9_6, QT_5_9_7, QT_5_9_8, QT_5_9_9, QT_5_10_0, 
QT_5_10_1, QT_5_11_0, QT_5_11_1, QT_5_11_2, QT_5_11_3, QT_5_12_0, QT_5_12_1, QT_5_12_2, QT_5_12_3, QT_5_12_4, QT_5_12_5,
 QT_5_12_6, QT_5_12_7, QT_5_12_8, QT_5_12_9, QT_5_12_10, QT_5_12_11, QT_5_12_12, QT_5_13_0, QT_5_13_1, QT_5_13_2, 
QT_5_14_0, QT_5_14_1, QT_5_14_2, QT_5_15_0, QT_5_15_1, QT_5_15_2, QT_6_0_0, QT_6_0_1, QT_6_0_2, QT_6_0_3, QT_6_0_4, 
QT_6_1_0, QT_6_1_1, QT_6_1_2, QT_6_1_3, QT_6_2_0, QT_6_2_1, QT_6_2_2, QT_6_2_3, QT_6_2_4, QT_6_3_0, QT_6_3_1, QT_6_4_0]

MINGW = 'mingw'

MSVC = 'msvc'

MSVC_2017 = 'msvc2017'
MSVC_2019 = 'msvc2019'
MSVC_2022 = 'msvc2022'

ARCH_32 = "i686"
ARCH_64 = "x86_64"


MINGW_11_2_0 = "mingw11.2.0"
MINGW_8_1_0 = "mingw8.1.0"
MINGW_7_3_0 = "mingw7.3.0"
MINGW_5_3_0 = "mingw5.3.0"
MINGW_4_9_2 = "mingw4.9.2"

MINGW_4_9_1 = "mingw4.9.1"
MINGW_4_8_2 = "mingw4.8.2"
MINGW_4_8_0 = "mingw4.8.0"
MINGW_4_7_2 = "mingw4.7.2"


# generated
QT_TO_MINGW32 = {QT_5_9_0: MINGW_5_3_0, QT_5_9_1: MINGW_5_3_0, QT_5_9_2: MINGW_5_3_0, QT_5_9_3: MINGW_5_3_0, QT_5_9_4: 
MINGW_5_3_0, QT_5_9_5: MINGW_5_3_0, QT_5_9_6: MINGW_5_3_0, QT_5_9_7: MINGW_5_3_0, QT_5_9_8: MINGW_5_3_0, QT_5_9_9: 
MINGW_5_3_0, QT_5_10_0: MINGW_5_3_0, QT_5_10_1: MINGW_5_3_0, QT_5_11_0: MINGW_5_3_0, QT_5_11_1: MINGW_5_3_0, QT_5_11_2: 
MINGW_5_3_0, QT_5_11_3: MINGW_5_3_0, QT_5_12_2: MINGW_7_3_0, QT_5_12_3: MINGW_7_3_0, QT_5_12_4: MINGW_7_3_0, QT_5_12_5: 
MINGW_7_3_0, QT_5_12_6: MINGW_7_3_0, QT_5_12_7: MINGW_7_3_0, QT_5_12_8: MINGW_7_3_0, QT_5_12_9: MINGW_7_3_0, QT_5_12_10:
 MINGW_7_3_0, QT_5_12_11: MINGW_7_3_0, QT_5_12_12: MINGW_7_3_0, QT_5_13_0: MINGW_7_3_0, QT_5_13_1: MINGW_7_3_0, 
QT_5_13_2: MINGW_7_3_0, QT_5_14_0: MINGW_7_3_0, QT_5_14_1: MINGW_7_3_0, QT_5_14_2: MINGW_7_3_0, QT_5_15_0: MINGW_8_1_0, 
QT_5_15_1: MINGW_8_1_0, QT_5_15_2: MINGW_8_1_0}
QT_TO_MINGW64 = {QT_5_12_0: MINGW_7_3_0, QT_5_12_1: MINGW_7_3_0, QT_5_12_2: MINGW_7_3_0, QT_5_12_3: MINGW_7_3_0, 
QT_5_12_4: MINGW_7_3_0, QT_5_12_5: MINGW_7_3_0, QT_5_12_6: MINGW_7_3_0, QT_5_12_7: MINGW_7_3_0, QT_5_12_8: MINGW_7_3_0, 
QT_5_12_9: MINGW_7_3_0, QT_5_12_10: MINGW_7_3_0, QT_5_12_11: MINGW_7_3_0, QT_5_12_12: MINGW_7_3_0, QT_5_13_0: 
MINGW_7_3_0, QT_5_13_1: MINGW_7_3_0, QT_5_13_2: MINGW_7_3_0, QT_5_14_0: MINGW_7_3_0, QT_5_14_1: MINGW_7_3_0, QT_5_14_2: 
MINGW_7_3_0, QT_5_15_0: MINGW_8_1_0, QT_5_15_1: MINGW_8_1_0, QT_5_15_2: MINGW_8_1_0, QT_6_0_0: MINGW_8_1_0, QT_6_0_1: 
MINGW_8_1_0, QT_6_0_2: MINGW_8_1_0, QT_6_0_3: MINGW_8_1_0, QT_6_0_4: MINGW_8_1_0, QT_6_1_0: MINGW_8_1_0, QT_6_1_1: 
MINGW_8_1_0, QT_6_1_2: MINGW_8_1_0, QT_6_1_3: MINGW_8_1_0, QT_6_2_0: MINGW_8_1_0, QT_6_2_1: MINGW_8_1_0, QT_6_2_2: 
MINGW_11_2_0, QT_6_2_3: MINGW_11_2_0, QT_6_2_4: MINGW_11_2_0, QT_6_3_0: MINGW_11_2_0, QT_6_3_1: MINGW_11_2_0, QT_6_4_0: 
MINGW_11_2_0}
def qt_mingw_compiler(qt, arch):
    if arch == ARCH_32:
        return QT_TO_MINGW32.get(qt)
    else:
        return QT_TO_MINGW64.get(qt)

# generated
QT_TO_MSVC2019_32 = [QT_5_15_0, QT_5_15_1, QT_5_15_2]
QT_TO_MSVC2019_64 = [QT_5_15_0, QT_5_15_1, QT_5_15_2, QT_6_0_0, QT_6_0_1, QT_6_0_2, QT_6_0_3, QT_6_0_4, QT_6_1_0, 
QT_6_1_1, QT_6_1_2, QT_6_1_3, QT_6_2_0, QT_6_2_1, QT_6_2_2, QT_6_2_3, QT_6_2_4, QT_6_3_0, QT_6_3_1, QT_6_4_0]
def is_msvc2019_optimal(qt, compiler, arch):
    if arch == ARCH_32:
        return qt in QT_TO_MSVC2019_32
    else:
        return qt in QT_TO_MSVC2019_64


class folded_str(str): pass
class literal_str(str): pass
def folded_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>')
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(folded_str, folded_str_representer)
yaml.add_representer(literal_str, literal_str_representer)

def pack(cmds, name, local):
    if local:
        return "rem {}\n".format(name) + "\n".join(cmds) + "\n"
    else:
        return {
            "name": name, 
            "shell": "cmd", 
            "run": literal_str("\n".join(cmds) + "\n")
        }

def arch_suffix(arch):
    return {
        ARCH_32: '_32',
        ARCH_64: '_64',
    }[arch]

def to_version(s):
    m = re.match("([0-9.]+)", s)
    return version.parse(m.group(1))

def is_mingw(compiler):
    if compiler is None:
        return False
    return compiler.startswith("mingw")

def is_msvc(compiler):
    if compiler is None:
        return False
    return compiler.startswith("msvc")

def compiler_prefix(compiler, arch, dot = False):
    if dot:
        return compiler + "-" + arch
    if is_msvc(compiler):
        return compiler + arch_suffix(arch)
    v = to_version(compiler)
    return 'mingw' + str(v.major) + str(v.minor) + arch_suffix(arch)

def to_qt(qt):
    if not qt.startswith("qt"):
        return "qt" + qt
    return qt

def to_qwt(qwt):
    if not qwt.startswith('qwt'):
        return 'qwt' + qwt
    return qwt

def to_compiler(qt, compiler, arch):
    if compiler == MSVC:
        return MSVC_2019
    if compiler == MINGW:
        return qt_mingw_compiler(qt, arch)
    return compiler

def to_arch(arch):
    return {
        "32": ARCH_32,
        "64": ARCH_64,
        ARCH_32: ARCH_32,
        ARCH_64: ARCH_64
    }[arch]


COMMUNITY = "Community"
ENTERPRISE = "Enterprise"

def vcvars_path(compiler, edition, arch):
    if compiler == MSVC_2019:
        return "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\{}\\VC\\Auxiliary\\Build\\vcvars{}.bat".format(edition, "32" if arch == ARCH_32 else "64")
    elif compiler == MSVC_2022:
        return "C:\\Program Files\\Microsoft Visual Studio\\2022\\{}\\VC\\Auxiliary\\Build\\vcvars{}.bat".format(edition, "32" if arch == ARCH_32 else "64")

QWT_6_2_0 = "qwt6.2.0"

QWTS = [QWT_6_2_0]

def qwt_url(qwt):
    return {
        QWT_6_2_0: 'https://altushost-swe.dl.sourceforge.net/project/qwt/qwt/6.2.0/qwt-6.2.0.zip'
    }[qwt]

def install_aqt_step(local):
    pass

def flavour(qwt, qt, compiler, arch):
    return 

def filter_optimal(flavours):
    res = []
    for qwt, qt, compiler, arch in flavours:
        qwt = to_qwt(qwt)
        if qwt not in QWTS:
            continue
        qt = to_qt(qt)
        arch = to_arch(arch)
        compiler = to_compiler(qt, compiler, arch)
        if compiler is None:
            continue
        if compiler == MSVC_2019:
            if is_msvc2019_optimal(qt, compiler, arch):
                res.append((qwt, qt, compiler, arch))
        else:
            res.append((qwt, qt, compiler, arch))
    return res
    

def download(url, name = None):
    if name is None:
        name = os.path.basename(url)
    return 'if not exist "{}" curl -L -o {} "{}"'.format(name, name, url.replace("%", "%%"))

def set_path(*args):
    paths = []
    for arg in args:
        if isinstance(arg, str):
            paths.append(arg)
        elif arg is None:
            pass
        elif isinstance(arg, list):
            for arg_ in arg:
                paths.append(arg_)
        else:
            raise ValueError('not list none or string', arg)
    paths.append('%PATH%')
    return "set PATH={}".format(";".join(paths))

def mkdir(path):
    return "if not exist \"{}\" mkdir \"{}\"".format(path,path)

def copy_file(src, dst):
    return "copy /y \"{}\" \"{}\"".format(src.replace("/","\\"), dst.replace("/","\\"))

def rmdir(path):
    return 'if exist {} rmdir /q /s {}'.format(path, path)

def extract(path, test = None):
    if test:
        return 'if not exist \"{}\" 7z x -y \"{}\"'.format(test, path)
    return '7z x -y \"{}\"'.format(path)

def archive(dst, src):
    return "7z a \"{}\" \"{}\"".format(dst, src)

def mingw_toolname(compiler, arch):
    if compiler == MINGW_11_2_0:
        if arch == ARCH_64:
            return ('tools_mingw90', 'qt.tools.win64_mingw900')
        return None
    else:
        return ('tools_mingw', 'qt.tools.' + {ARCH_32: 'win32', ARCH_64: 'win64'}[arch] + "_" + compiler.replace(".", ""))

def qt_dist_arch(compiler, arch):
    if compiler == MSVC_2019:
        return {ARCH_32: 'win32_msvc2019', ARCH_64: 'win64_msvc2019_64'}[arch]
    if is_mingw(compiler):
        if compiler == MINGW_11_2_0:
            return 'win64_mingw'
        maj_, min_, fix_ = compiler.replace("mingw","").split('.')
        return {ARCH_32: 'win32', ARCH_64: 'win64'}[arch] + "_mingw{}{}".format(maj_, min_)


def qt_bin_path(qt, compiler, arch):
    qt_ = qt.replace("qt","")

    def bin(spec):
        return os.path.join(qt_, spec, "bin")

    if compiler == MINGW_11_2_0:
        if arch == ARCH_64:
            return bin("mingw_64")
        else:
            return None
    if compiler == MSVC_2019:
        if arch == ARCH_32:
            return bin("msvc2019")
        else:
            return bin("msvc2019_64")
    maj, min, fix = compiler.replace("mingw","").split(".")
    return  bin("mingw{}{}_{}".format(maj, min, {ARCH_32: '32', ARCH_64: '64'}[arch]))

def mingw_bin_path(compiler, arch):
    if not is_mingw(compiler):
        return None
    return os.path.join('Tools', compiler.replace(".","") + "_" + {ARCH_32: '32', ARCH_64: '64'}[arch], "bin")

def qwt_local_path(qwt):
    return "C:\\Qwt-" + qwt.replace("qwt","")

def qwt_flavour_name(qwt, qt, compiler, arch):
    return "-".join([qwt, qt, compiler, arch])

def build_step(qwt, qt, compiler, arch, local):

    cmds = []
    if local:
        python_path = ["C:\\Miniconda3","C:\\Miniconda3\\Scripts"]
    else:
        python_path = ["C:\\Miniconda","C:\\Miniconda\\Scripts"]

    def path_join(*args):
        for arg in args:
            if arg is None:
                return None
        return os.path.join(*args)

    cmds.append(set_path(
        python_path, 
        path_join("%CD%", qt_bin_path(qt, compiler, arch)), 
        path_join("%CD%", mingw_bin_path(compiler, arch)))
    )

    cmds.append("where aqt || exit /b")

    if is_mingw(compiler):
        # install mingw
        cat, name = mingw_toolname(compiler, arch)
        gcc = os.path.join(mingw_bin_path(compiler, arch), "gcc.exe")
        cmds.append('if not exist {} aqt install-tool windows desktop {} {}'.format(gcc, cat, name))
    else:
        pass

    # install qt
    arch_ = qt_dist_arch(compiler, arch)

    qmake = os.path.join(qt_bin_path(qt, compiler, arch), "qmake.exe")
    cmds.append('if not exist {} aqt install-qt windows desktop {} {}'.format(qmake, qt.replace("qt", ""), arch_))

    # download qwt
    url = qwt_url(qwt)
    name = os.path.basename(url)
    qwt_dir_name = os.path.splitext(name)[0]
    cmds.append(download(url, name))
    cmds.append(rmdir(qwt_dir_name))
    cmds.append(extract(name))

    if is_msvc(compiler):
        vcvars = vcvars_path(compiler, COMMUNITY if local else ENTERPRISE, arch)
        cmds.append("set INCLUDE=")
        cmds.append("call \"{}\"".format(vcvars))

    cmds.append("where qmake || exit /b")
    if is_mingw(compiler):
        cmds.append("where gcc || exit /b")
    else:
        cmds.append("where cl || exit /b")

    # build qwt
    cmds.append("pushd {}".format(qwt_dir_name))
    cmds.append("qmake")
    if is_mingw(compiler):
        cmds.append("mingw32-make")
        cmds.append("mingw32-make install")
    else:
        cmds.append("nmake")
        cmds.append("nmake install")
    cmds.append("popd")

    local_path = qwt_local_path(qwt)

    flavour_base = qwt_flavour_name(qwt, qt, compiler, arch)
    zip_name = flavour_base + ".zip"
    cmds.append(archive(zip_name, local_path))
    cmds.append(rmdir(local_path))

    return pack(cmds, "flavour {} {} {} {}".format(qwt, qt, compiler, arch), local)

class Dumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # disable resolving on as tag:yaml.org,2002:bool (disable single quoting)
        cls = self.__class__
        cls.yaml_implicit_resolvers['o'] = []

def install_aqt_step(local):
    cmds = []
    if local:
        python_path = ["C:\\Miniconda3","C:\\Miniconda3\\Scripts"]
    else:
        python_path = ["C:\\Miniconda","C:\\Miniconda\\Scripts"]
    cmds.append(set_path(python_path))
    cmds.append("where aqt || pip install aqtinstall")
    return pack(cmds, "install aqt", local)

def testenv_step(local):
    cmds = []
    cmds.append('where curl || exit /b')
    cmds.append('where 7z || exit /b')
    #cmds.append('where ninja')
    return pack(cmds, "test env", local)


class ReleaseStep:
    def __init__(self):
        self._artifacts = []

    def add(self, artifact):
        self._artifacts.append(artifact)

    def github(self):
        return {
            "uses": "ncipollo/release-action@v1",
            "if": "startsWith(github.ref, 'refs/tags/')",
            "with": {
                "artifacts": literal_str("\n".join(self._artifacts) + "\n"),
                "token": "${{ secrets.GITHUB_TOKEN }}"
            }
        }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--qt', nargs='+', help="qt versions to build")
    parser.add_argument('--qwt', nargs='+', help="qwt versions to build")
    parser.add_argument('--arch', nargs='+', help="architectures to build (32 or 64 or both)")
    parser.add_argument('--compiler', nargs='+', help="compiler(s) to use (msvc, mingw)")

    args = parser.parse_args()

    qwts = []
    compilers = []
    archs = []
    qts = []

    if args.qwt is None:
        qwts = [QWT_6_2_0]
    else:
        qwts = args.qwt
    if args.qt is None:
        qts = [QT_5_15_2, QT_6_4_0]
    else:
        qts = args.qt
    if args.compiler is None:
        compilers = [MINGW, MSVC]
    else:
        compilers = args.compiler
    if args.arch is None:
        archs = [ARCH_32, ARCH_64]
    else:
        archs = args.arch

    steps_local = []
    steps_github = []

    steps_local.append(install_aqt_step(local=True))
    steps_github.append(install_aqt_step(local=False))

    steps_local.append(testenv_step(local=True))
    steps_github.append(testenv_step(local=False))

    release_step = ReleaseStep()

    for qwt, qt, compiler, arch in filter_optimal(product(qwts, qts, compilers, archs)):
        steps_local.append(build_step(qwt, qt, compiler, arch, local=True))
        steps_github.append(build_step(qwt, qt, compiler, arch, local=False))
        
        flavour_base = qwt_flavour_name(qwt, qt, compiler, arch)
        zip_name = flavour_base + ".zip"
        
        release_step.add(zip_name)

    steps_github.append(release_step.github())

    workflow_path = os.path.join(os.path.dirname(__file__), ".github", "workflows", "main.yml")

    batch_path = os.path.join(os.path.dirname(__file__), "main.bat")

    os.makedirs(os.path.dirname(workflow_path), exist_ok=True)

    data = {"name":"main","on":{"push":{"tags":"*"}},"jobs":{"main": {"runs-on":"windows-2019","steps":steps_github}}}
    with open(workflow_path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(data, None, Dumper=Dumper, sort_keys=False))
    with open(batch_path, 'w', encoding='utf-8') as f:
        f.write("@echo off\n" + "\n".join(steps_local) + "\n")

if __name__ == "__main__":
    main()
