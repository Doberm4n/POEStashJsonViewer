# POEStashJsonViewer (offline parse, view and search stash and character inventory item json data)

This app accepts user-saved .json file(s) after using PoE API.

Features:

- open one or multiple .json files;
- open single json files, created with this app for faster loading data;
- show item location, properties, modifiers and so on;
- calculating different values for items (DPS, resistances, attributes, sockets, Life/Mana and so on);
- column selection and sorting;
- creating, saving, loading and applying filters (note: using only AND statement between conditions);
- exporting all data to csv, SQLite Database (you can use advanced filtering by using SQLite DB managers) and single json file (for faster next load);
- exporting view to csv;
- relatively fast (tested on ~7000 items).

![alt text](https://github.com/Doberm4n/POEStashJsonViewer/blob/master/screenshots/columnsSelectWindow_1.png)

Notes:

- POEStashJsonViewer is offline app;
- POEStashJsonViewer curently is alpha, so you may encounter some bugs;
- You can report bugs on GitHub - https://github.com/Doberm4n/POEStashJsonViewer;
- As usual if there is a problem with parsing of specific item all I need is a .json file to check.

Download:

1. You can run app from sources (requirements: Python 2.7, PyQt4) (https://github.com/Doberm4n/POEStashJsonViewer);
or
2. You can download standalone package with .exe, builded with PyInstaller (https://github.com/Doberm4n/POEStashJsonViewer/releases).

