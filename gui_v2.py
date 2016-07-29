# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(583, 270)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gpio_Box = QtGui.QGroupBox(self.centralwidget)
        self.gpio_Box.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.gpio_Box.setObjectName(_fromUtf8("gpio_Box"))
        self.excGpio = QtGui.QPushButton(self.gpio_Box)
        self.excGpio.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.excGpio.setObjectName(_fromUtf8("excGpio"))
        self.labOut = QtGui.QLabel(self.gpio_Box)
        self.labOut.setGeometry(QtCore.QRect(100, 30, 81, 16))
        self.labOut.setObjectName(_fromUtf8("labOut"))
        self.combInp = QtGui.QComboBox(self.gpio_Box)
        self.combInp.setGeometry(QtCore.QRect(10, 50, 76, 22))
        self.combInp.setObjectName(_fromUtf8("combInp"))
        self.combInp.addItem(_fromUtf8(""))
        self.combInp.addItem(_fromUtf8(""))
        self.labInp = QtGui.QLabel(self.gpio_Box)
        self.labInp.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.labInp.setObjectName(_fromUtf8("labInp"))
        self.combOut = QtGui.QComboBox(self.gpio_Box)
        self.combOut.setGeometry(QtCore.QRect(100, 50, 76, 22))
        self.combOut.setObjectName(_fromUtf8("combOut"))
        self.combOut.addItem(_fromUtf8(""))
        self.canGpio = QtGui.QPushButton(self.gpio_Box)
        self.canGpio.setGeometry(QtCore.QRect(190, 50, 75, 23))
        self.canGpio.setObjectName(_fromUtf8("canGpio"))
        self.gpio_Box_2 = QtGui.QGroupBox(self.centralwidget)
        self.gpio_Box_2.setGeometry(QtCore.QRect(10, 100, 271, 81))
        self.gpio_Box_2.setObjectName(_fromUtf8("gpio_Box_2"))
        self.pushGpio_5 = QtGui.QPushButton(self.gpio_Box_2)
        self.pushGpio_5.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.pushGpio_5.setObjectName(_fromUtf8("pushGpio_5"))
        self.labOut_5 = QtGui.QLabel(self.gpio_Box_2)
        self.labOut_5.setGeometry(QtCore.QRect(100, 30, 81, 16))
        self.labOut_5.setObjectName(_fromUtf8("labOut_5"))
        self.combInp_5 = QtGui.QComboBox(self.gpio_Box_2)
        self.combInp_5.setGeometry(QtCore.QRect(10, 50, 76, 22))
        self.combInp_5.setObjectName(_fromUtf8("combInp_5"))
        self.combInp_5.addItem(_fromUtf8(""))
        self.labInp_5 = QtGui.QLabel(self.gpio_Box_2)
        self.labInp_5.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.labInp_5.setObjectName(_fromUtf8("labInp_5"))
        self.combOut_5 = QtGui.QComboBox(self.gpio_Box_2)
        self.combOut_5.setGeometry(QtCore.QRect(100, 50, 76, 22))
        self.combOut_5.setObjectName(_fromUtf8("combOut_5"))
        self.combOut_5.addItem(_fromUtf8(""))
        self.pushGpio_7 = QtGui.QPushButton(self.gpio_Box_2)
        self.pushGpio_7.setGeometry(QtCore.QRect(190, 50, 75, 23))
        self.pushGpio_7.setObjectName(_fromUtf8("pushGpio_7"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(290, 20, 271, 161))
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.btnQuit = QtGui.QMenu(self.menubar)
        self.btnQuit.setObjectName(_fromUtf8("btnQuit"))
        self.btnSave = QtGui.QMenu(self.menubar)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.btnInit = QtGui.QMenu(self.menubar)
        self.btnInit.setObjectName(_fromUtf8("btnInit"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.btnSave.menuAction())
        self.menubar.addAction(self.btnInit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.btnQuit.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow", None))
        self.gpio_Box.setTitle(_translate("mainWindow", "SIngle Digital GPIO", None))
        self.excGpio.setText(_translate("mainWindow", "실행", None))
        self.labOut.setText(_translate("mainWindow", "Output Port", None))
        self.combInp.setItemText(0, _translate("mainWindow", "23", None))
        self.combInp.setItemText(1, _translate("mainWindow", "123", None))
        self.labInp.setText(_translate("mainWindow", "Input Port", None))
        self.combOut.setItemText(0, _translate("mainWindow", "23", None))
        self.canGpio.setText(_translate("mainWindow", "취소", None))
        self.gpio_Box_2.setTitle(_translate("mainWindow", "SIngle Digital GPIO", None))
        self.pushGpio_5.setText(_translate("mainWindow", "실행", None))
        self.labOut_5.setText(_translate("mainWindow", "Output Port", None))
        self.combInp_5.setItemText(0, _translate("mainWindow", "23", None))
        self.labInp_5.setText(_translate("mainWindow", "Input Port", None))
        self.combOut_5.setItemText(0, _translate("mainWindow", "23", None))
        self.pushGpio_7.setText(_translate("mainWindow", "취소", None))
        self.menu.setTitle(_translate("mainWindow", "설정", None))
        self.btnQuit.setTitle(_translate("mainWindow", "종료", None))
        self.btnSave.setTitle(_translate("mainWindow", "저장", None))
        self.btnInit.setTitle(_translate("mainWindow", "초기화", None))

