# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bbox.ui'
#
# Created: Wed Aug 14 15:54:44 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_bBox(object):
    def setupUi(self, bBox):
        bBox.setObjectName(_fromUtf8("bBox"))
        bBox.resize(414, 111)
        self.inputString = QtGui.QLineEdit(bBox)
        self.inputString.setGeometry(QtCore.QRect(10, 30, 401, 31))
        self.inputString.setObjectName(_fromUtf8("inputString"))
        self.label = QtGui.QLabel(bBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.buttonBox = QtGui.QDialogButtonBox(bBox)
        self.buttonBox.setGeometry(QtCore.QRect(320, 70, 91, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.updateMap = QtGui.QPushButton(bBox)
        self.updateMap.setGeometry(QtCore.QRect(10, 70, 95, 31))
        self.updateMap.setObjectName(_fromUtf8("updateMap"))

        self.retranslateUi(bBox)
        QtCore.QMetaObject.connectSlotsByName(bBox)

    def retranslateUi(self, bBox):
        bBox.setWindowTitle(QtGui.QApplication.translate("bBox", "bBox", None, QtGui.QApplication.UnicodeUTF8))
        self.inputString.setText(QtGui.QApplication.translate("bBox", "MinX,MinY,MaxX,MaxY", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("bBox", "Enter bbox as string", None, QtGui.QApplication.UnicodeUTF8))
        self.updateMap.setText(QtGui.QApplication.translate("bBox", "Update Map", None, QtGui.QApplication.UnicodeUTF8))

