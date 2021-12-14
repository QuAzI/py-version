python version.py > version.rc
pyinstaller --onefile ./application.py --version-file=version.rc
rem del version.rc
@pause