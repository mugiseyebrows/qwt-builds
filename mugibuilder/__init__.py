import os
import yaml
from packaging import version
import re

ON_PUSH = 1
ON_TAG = 2
WINDOWS_2019 = "windows-2019"

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

class folded_str(str): pass
class literal_str(str): pass
def folded_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>')
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(folded_str, folded_str_representer)
yaml.add_representer(literal_str, literal_str_representer)

class Dumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # disable resolving on as tag:yaml.org,2002:bool (disable single quoting)
        cls = self.__class__
        cls.yaml_implicit_resolvers['o'] = []

def save_workflow(path, steps, on = ON_TAG, runs_on = WINDOWS_2019):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if on == ON_TAG:
        on_ = {"push":{"tags":"*"}}
    else:
        on_ = "push"
    data = {"name":"main","on":on_,"jobs":{"main": {"runs-on":runs_on,"steps":steps}}}
    with open(path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(data, None, Dumper=Dumper, sort_keys=False))

def save_batch(path, steps):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("@echo off\n" + "\n".join(steps) + "\n")

class ReleaseStep:
    def __init__(self):
        self._artifacts = []

    def add(self, artifact):
        self._artifacts.append(artifact)

    def github(self, sorted = False):
        if sorted:
            self._artifacts.sort()
        return {
            "uses": "ncipollo/release-action@v1",
            "if": "startsWith(github.ref, 'refs/tags/')",
            "with": {
                "artifacts": literal_str("\n".join(self._artifacts) + "\n"),
                "token": "${{ secrets.GITHUB_TOKEN }}"
            }
        }

def pack_step(cmds, name, local):
    if local:
        return "rem {}\n".format(name) + "\n".join(cmds) + "\n"
    else:
        return {
            "name": name, 
            "shell": "cmd", 
            "run": literal_str("\n".join(cmds) + "\n")
        }

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


class Commander:
    
    def __init__(self, name, qt = None, compiler = None, arch = None, local = True):
        self._cmds = []
        self._path1 = set()
        self._path2 = set()
        self._use_aqt = False
        self._name = name

        self._local = local
        self._spec = qt, compiler, arch
        self._vcvars_called = False
    
    def start_commands(self):
        paths = list(self._path1) + list(self._path2)
        if len(paths) == 0:
            return []
        return [set_path(*paths)]

    def test_env(self, apps):
        for app in apps:
            self._cmds.append("where {} || exit /b".format(app))

    def add_python_path(self):
        def pp(*paths):
            res = []
            for path in paths:
                res.append(path)
                res.append(os.path.join(path, "Scripts"))
            return res
        if self._local:
            python_path = pp(
                "C:\\Miniconda3",
                "%HOMEPATH%\\Miniconda3",
                "%LOCALAPPDATA%\\Programs\\Python\\Python39",
                "%LOCALAPPDATA%\\Programs\\Python\\Python310",
            )
        else:
            python_path = pp("C:\\Miniconda")

        for path in python_path:
            self._path2.add(path)

    def add_qt_path(self):
        qt, compiler, arch = self._spec
        path = os.path.join("%CD%", qt_bin_path(qt, compiler, arch))
        self._path1.add(path)

    def add_mingw_path(self):
        qt, compiler, arch = self._spec
        path = os.path.join("%CD%", mingw_bin_path(compiler, arch))
        self._path1.add(path)

    def add_7z_path(self):
        self._path2.add("C:\\Program Files\\7-Zip")

    def add_curl_path(self):
        self._path2.add("C:\\Program Files\\Git\\mingw64\\bin")

    def pip_install_aqtinstall(self, test = True):
        if test:
            self._cmds.append("where aqt || pip install aqtinstall")
        else:
            self._cmds.append("pip install aqtinstall")
        self.add_python_path()

    def aqt_install_qt(self, test = True):
        qt, compiler, arch = self._spec
        arch_ = qt_dist_arch(compiler, arch)
        if test:
            qmake = os.path.join(qt_bin_path(qt, compiler, arch), "qmake.exe")
            test_ = "if not exist {} ".format(qmake)
        else:
            test_ = ""
        self._cmds.append('{}aqt install-qt windows desktop {} {}'.format(test_, qt.replace("qt", ""), arch_))
        self.add_python_path()
        self.add_qt_path()

    def aqt_install_mingw(self, test = True):
        qt, compiler, arch = self._spec
        if not is_mingw(compiler):
            return
        cat, name = mingw_toolname(compiler, arch)
        if test:
            gcc = os.path.join(mingw_bin_path(compiler, arch), "gcc.exe")
            test_ = "if not exist {} ".format(gcc)
        else:
            test_ = ""
        self._cmds.append('{}aqt install-tool windows desktop {} {}'.format(test_, cat, name))
        self.add_python_path()
        self.add_mingw_path()

    def download(self, url, test = True):
        name = os.path.basename(url)
        if test:
            cmd = download(url, name)
        else:
            cmd = download(url)
        self._cmds.append(cmd)
        name_without_ext = os.path.splitext(name)[0]
        self.add_curl_path()
        return name, name_without_ext
        
    def rmdir(self, name):
        self._cmds.append(rmdir(name))

    def extract(self, name, test = False):
        name_without_ext = os.path.splitext(name)[0]
        if test:
            cmd = extract(name, name_without_ext)
        else:
            cmd = extract(name)
        self._cmds.append(cmd)
        self.add_7z_path()
        return name_without_ext

    def call_vcvars(self, clear_include = True):
        self._vcvars_called = True
        qt, compiler, arch = self._spec
        local = self._local
        if not is_msvc(compiler):
            return
        vcvars = vcvars_path(compiler, COMMUNITY if local else ENTERPRISE, arch)
        if clear_include:
            self._cmds.append("set INCLUDE=")
        self._cmds.append("call \"{}\"".format(vcvars))

    def pushd(self, name):
        self._cmds.append("pushd {}".format(name))

    def popd(self):
        self._cmds.append("popd")

    def qmake(self):
        self._cmds.append("qmake")

    def make_install(self):
        qt, compiler, arch = self._spec
        if is_mingw(compiler):
            self._cmds.append("mingw32-make install")
        else:
            self._cmds.append("nmake install")

    def archive(self, dst, src):
        self._cmds.append(archive(dst, src))
        self.add_7z_path()

    def pack(self):
        qt, compiler, arch = self._spec
        if is_msvc(compiler) and not self._vcvars_called:
            print("warning: vcvars was not called")
        return pack_step(self.start_commands() + self._cmds, self._name, self._local)

def filter_specs(specs):
    res = []
    for qt, compiler, arch in specs:
        qt = to_qt(qt)
        arch = to_arch(arch)
        compiler = to_compiler(qt, compiler, arch)

        if compiler is None:
            continue
        if compiler == MSVC_2019:
            if is_msvc2019_optimal(qt, compiler, arch):
                res.append((qt, compiler, arch))
            else:
                #print("msvc2019 not optimal")
                pass
        else:
            res.append((qt, compiler, arch))
    return res

def add_spec_args(parser):
    parser.add_argument('--qt', nargs='+', help="qt versions to build")
    parser.add_argument('--arch', nargs='+', help="architectures to build (32 or 64 or both)")
    parser.add_argument('--compiler', nargs='+', help="compiler(s) to use (msvc, mingw)")

def get_specs(args):
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
    return qts, compilers, archs