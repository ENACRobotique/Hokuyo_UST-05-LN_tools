from PyQt5 import QtCore
import time
import numpy as np
import random
import ust05ln

class UstReader(QtCore.QThread):

    data_change = QtCore.pyqtSignal()

    def __init__(self,data,mutex,dataP):
        QtCore.QThread.__init__(self)
        self.data = data
        self.dataP = dataP
        self.mutex = mutex
        self.ust = ust05ln.UST(port = "/dev/ttyACM0")
        self.is_running = False
        self.start_now = False
        self.stop_now = False

    def __del__(self):
        self.wait()

    def run(self):
        try:
            while True :
                if self.start_now :
                    self.ust.start_ranging()
                    self.start_now  = False
                    self.is_running = True

                if self.stop_now :
                    self.ust.stop_ranging()
                    self.stop_now = False
                    self.is_running = False
                    
                if self.is_running :
                    self.mutex.lock()
                    data = self.ust.get_measures()
                    if data is not None:
                        self.data[:] = data[1]
                        self.dataP[:] = data[2]
                    self.mutex.unlock()
                    if data is not None:
                        self.data_change.emit()
        finally:
            self.ust.stop()
            
    def start_ranging(self) :
        self.start_now = True


    def stop_ranging(self) :
        self.stop_now = True
