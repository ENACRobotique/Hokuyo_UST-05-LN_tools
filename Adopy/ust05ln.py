#!/usr/bin/python3
from serial import Serial
import time
from collections import namedtuple
import numpy as np
import sys
import re

NB_POINTS = 541

class UST:
    
    Command = namedtuple('Command',['command', 'answer_expected', 'answer'])

    START_RANGING = Command('#GT15466', False, '')
    STOP_RANGING = Command('#ST5297', True, '#ST00A845')
    ID = Command('#IN0D54', True, '')
    ID2 = Command('#CLC2DD', True, '')

    PLOP = Command('#GR0EEE1', True, '')

    def __init__(self, port="/dev/ttyACM0", baudrate=115200):
        self.ser = Serial(port, baudrate)
        self.stop_ranging()
        self.timestamp = 0
        self.distances = np.zeros(NB_POINTS,dtype="uint16")
        self.puissances = np.zeros(NB_POINTS,dtype="uint16")
        self.regex = re.compile(b'^#GT00:([0-9A-F]+):[0-9A-F]+:([0-9A-F]{4328})[0-9A-F]{4}$')

    def send_command(self, command, timeout=2):
        self.ser.write(command.command.encode()+b'\n')    # writes command to LIDAR
        self.ser.reset_input_buffer()
        data = b''
        start_time = time.time()
        if command.answer_expected and command.answer != '':    #precise answer expected, search for it !
            while time.time() - start_time < timeout:
                if self.ser.in_waiting:
                    data+=self.ser.read()
                    data = data.split(b'\n')[-1]
                    if command.answer.encode() in data:
                        break
            return data
        elif command.answer_expected:   # answer expected but be don't known which : return the first one (until \n)
            while time.time() - start_time < timeout:
                if self.ser.in_waiting:
                    data+=self.ser.read()
                    if b'\n' in data:
                        data = data.split(b'\n')[0]
                        break
            return data
        else:
            return b''

    def stop_ranging(self):
        self.send_command(self.STOP_RANGING)

    def start_ranging(self):
        self.stop_ranging()
        self.send_command(self.START_RANGING)

    def stop(self):
        self.stop_ranging()
    
    def get_measures(self):
        """
        returns measures under the form (timestamp, [(distance, quality), ...])
        timestamp : time in seconds since the LIDAR startup
        distance range : 0 - 65635
        valur range : 0 - ??? (65635 max)
        eg: (102.123456, [(552, 1244), (646, 1216), (676, 1270), ...])
        """
        raw_bytes=self.ser.readline().strip()
        m = self.regex.match(raw_bytes) 
        if m is not None:
            tb = m.groups()[0]
            mesb = m.groups()[1]
            self.timestamp = int(tb, 16)/10**6
            self.distances = np.fromiter((int(mesb[i:i+4],16)  for i in range(0, NB_POINTS*8, 8)),dtype = np.uint16)
            self.puissances = np.fromiter((int(mesb[i:i+4],16)  for i in range(4, NB_POINTS*8, 8)),dtype = np.uint16)
            return (self.timestamp, self.distances, self.puissances)


if __name__ == "__main__":
    ust = UST(port = sys.argv[1])
    try:
        ret = ust.send_command(ust.ID)
        print(ret)
        ust.start_ranging()
        while True:
            if ust.get_measures() is not None:
                print(ust.distances)
    finally:
        ust.stop()

