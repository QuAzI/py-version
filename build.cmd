python ./src/version.py > version.rc
pyinstaller --onefile ./src/application.py --version-file=version.rc
del version.rc
@pause