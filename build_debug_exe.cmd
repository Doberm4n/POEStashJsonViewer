rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEStashJsonViewer.py --noupx --onedir --version-file=version.txt