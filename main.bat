@echo off
rem install aqtinstall
set PATH=C:\Miniconda3\Scripts;C:\Miniconda3;%PATH%
where aqt || pip install aqtinstall

rem flavour qwt6.1.3 qt5.11.3 mingw5.3.0 i686
set PATH=%CD%\Tools\mingw530_32\bin;%CD%\5.11.3\mingw53_32\bin;C:\Miniconda3\Scripts;C:\Miniconda3;C:\Program Files\Git\mingw64\bin;C:\Program Files\7-Zip;%PATH%
if not exist 5.11.3\mingw53_32\bin\qmake.exe aqt install-qt windows desktop 5.11.3 win32_mingw53
if not exist Tools\mingw530_32\bin\gcc.exe aqt install-tool windows desktop tools_mingw qt.tools.win32_mingw530
if not exist "qwt-6.1.3.zip" curl -L -o qwt-6.1.3.zip "https://cfhcable.dl.sourceforge.net/project/qwt/qwt/6.1.3/qwt-6.1.3.zip"
if exist qwt-6.1.3 rmdir /q /s qwt-6.1.3
7z x -y "qwt-6.1.3.zip"
pushd qwt-6.1.3
qmake
mingw32-make install
popd
7z a "qwt6.1.3-qt5.11.3-mingw5.3.0-i686.zip" "C:\Qwt-6.1.3"
if exist C:\Qwt-6.1.3 rmdir /q /s C:\Qwt-6.1.3

