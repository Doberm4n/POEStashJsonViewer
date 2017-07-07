rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POEWeaponDPS.py -w --version-file=version.txt