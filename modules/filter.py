# -*- coding: utf-8 -*-

class filterDialog(QtGui.QDialog, GUIAbout.Ui_Dialog):
    def __init__(self):
        global version
        global link
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.linkLabel.linkActivated.connect(self.openURL)
        self.versionLabel.setText("v." + version)
        self.linkLabel.setText(link)
        pic = self.picLabel
        pic.setPixmap(QtGui.QPixmap(":todo-icon32.png"))