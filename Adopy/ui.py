# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 591, 441))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.Data_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.Data_table.setLineWidth(1)
        self.Data_table.setObjectName(_fromUtf8("Data_table"))

        self.Data_table.setColumnCount(2)
        self.Data_table.setRowCount(541)

        for i in range(541) :
            item = QtWidgets.QTableWidgetItem()
            self.Data_table.setVerticalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem()
        self.Data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Data_table.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.Data_table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menucustom_area_designer = QtWidgets.QMenu(self.menubar)
        self.menucustom_area_designer.setObjectName(_fromUtf8("menucustom_area_designer"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menucustom_area_designer.menuAction())

        self.retranslateUi(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Start ranging", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop ranging", None))

        for i in range(541) :
            item = self.Data_table.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i), None))
       
        item = self.Data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Puissances", None))
        item = self.Data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Distances", None))
        self.menucustom_area_designer.setTitle(_translate("MainWindow", "menu", None))

