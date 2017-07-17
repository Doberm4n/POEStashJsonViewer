rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEStashTabViewer.py --noupx --onedir --version-file=version.txt