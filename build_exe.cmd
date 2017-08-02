rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEStashJsonViewer.py -w --noupx --onedir --icon=res\database-icon16.ico --version-file=version.txt