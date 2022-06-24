@echo off
rem install aqtinstall
set PATH=%LOCALAPPDATA%\Programs\Python\Python310;%LOCALAPPDATA%\Programs\Python\Python39\Scripts;%LOCALAPPDATA%\Programs\Python\Python310\Scripts;C:\Miniconda3;%HOMEPATH%\Miniconda3\Scripts;%HOMEPATH%\Miniconda3;C:\Miniconda3\Scripts;%LOCALAPPDATA%\Programs\Python\Python39;%PATH%
where aqt || pip install aqtinstall

rem flavour qwt6.2.0 qt6.4.0 mingw11.2.0 x86_64
set PATH=%CD%\Tools\mingw1120_64\bin;%CD%\6.4.0\mingw_64\bin;%LOCALAPPDATA%\Programs\Python\Python310;%LOCALAPPDATA%\Programs\Python\Python39\Scripts;%LOCALAPPDATA%\Programs\Python\Python310\Scripts;C:\Program Files\Git\mingw64\bin;C:\Miniconda3;%HOMEPATH%\Miniconda3\Scripts;%HOMEPATH%\Miniconda3;C:\Program Files\7-Zip;C:\Miniconda3\Scripts;%LOCALAPPDATA%\Programs\Python\Python39;%PATH%
if not exist 6.4.0\mingw_64\bin\qmake.exe aqt install-qt windows desktop 6.4.0 win64_mingw
if not exist Tools\mingw1120_64\bin\gcc.exe aqt install-tool windows desktop tools_mingw90 qt.tools.win64_mingw900
if not exist "qwt-6.2.0.zip" curl -L -o qwt-6.2.0.zip "https://altushost-swe.dl.sourceforge.net/project/qwt/qwt/6.2.0/qwt-6.2.0.zip"
if exist qwt-6.2.0 rmdir /q /s qwt-6.2.0
if exist C:\Qwt-6.2.0 rmdir /q /s C:\Qwt-6.2.0
7z x -y "qwt-6.2.0.zip"
pushd qwt-6.2.0
qmake
mingw32-make install
popd
7z a "qwt6.2.0-qt6.4.0-mingw11.2.0-x86_64.zip" "C:\Qwt-6.2.0"

rem flavour qwt6.2.0 qt6.4.0 msvc2019 x86_64
set PATH=%CD%\6.4.0\msvc2019_64\bin;%LOCALAPPDATA%\Programs\Python\Python310;%LOCALAPPDATA%\Programs\Python\Python39\Scripts;%LOCALAPPDATA%\Programs\Python\Python310\Scripts;C:\Program Files\Git\mingw64\bin;C:\Miniconda3;%HOMEPATH%\Miniconda3\Scripts;%HOMEPATH%\Miniconda3;C:\Program Files\7-Zip;C:\Miniconda3\Scripts;%LOCALAPPDATA%\Programs\Python\Python39;%PATH%
if not exist 6.4.0\msvc2019_64\bin\qmake.exe aqt install-qt windows desktop 6.4.0 win64_msvc2019_64
if not exist "qwt-6.2.0.zip" curl -L -o qwt-6.2.0.zip "https://altushost-swe.dl.sourceforge.net/project/qwt/qwt/6.2.0/qwt-6.2.0.zip"
if exist qwt-6.2.0 rmdir /q /s qwt-6.2.0
if exist C:\Qwt-6.2.0 rmdir /q /s C:\Qwt-6.2.0
7z x -y "qwt-6.2.0.zip"
set INCLUDE=
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
pushd qwt-6.2.0
qmake
nmake install
popd
7z a "qwt6.2.0-qt6.4.0-msvc2019-x86_64.zip" "C:\Qwt-6.2.0"

