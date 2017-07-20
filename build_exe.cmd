rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEStashJsonViewer.py -w --noupx --onedir --version-file=version.txt