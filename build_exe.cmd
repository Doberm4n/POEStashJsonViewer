rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEStashTabViewer.py -w --version-file=version.txt