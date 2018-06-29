import ui as U
from PyQt5 import QtCore, QtWidgets, QtGui
import ust_reader
import numpy as np
import drawing

class CAB (U.Ui_MainWindow) :

    def __init__(self, parent=None) :
        U.Ui_MainWindow.__init__(self)
        self.qtimer = QtCore.QTimer()
        self.data = np.zeros(541)
        self.dataP = np.zeros(541)
        self.mutex = QtCore.QMutex()
        self.reader = ust_reader.UstReader(self.data,self.mutex,self.dataP)

    def built(self):
        self.vue = drawing.DrawingWidget(self.data.copy(),self.horizontalLayoutWidget)
        self.vue.setMinimumSize(QtCore.QSize(237, 0))
        self.vue.setObjectName("vue")
        self.horizontalLayout.addWidget(self.vue)
        self.reader.data_change.connect(self.mafonction)
        self.reader.start()
        self.pushButton.clicked.connect(self.vue.flag_start)
        self.pushButton.clicked.connect(self.reader.start_ranging)
        self.pushButton_2.clicked.connect(self.reader.stop_ranging)
        self.pushButton_2.clicked.connect(self.vue.flag_stop)

    def mafonction(self) :
        self.mutex.lock()
        for i,(p,d) in enumerate(zip(self.dataP,self.data)) :
            itemP = QtWidgets.QTableWidgetItem(str(p))
            itemD = QtWidgets.QTableWidgetItem(str(d))
            if d > 6000 :
                itemP.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                itemD.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
            self.Data_table.setItem(i,0,itemP)
            self.Data_table.setItem(i,1,itemD)
            self.vue.update_with(self.data)
        self.mutex.unlock()


