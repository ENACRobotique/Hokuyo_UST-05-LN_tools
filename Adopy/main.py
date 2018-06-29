#!/usr/bin/python3
import cab as C
from PyQt5 import QtCore, QtWidgets, QtGui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    cab = C.CAB()
    cab.setupUi(MainWindow)
    cab.built()
    MainWindow.show()
    sys.exit(app.exec_())
