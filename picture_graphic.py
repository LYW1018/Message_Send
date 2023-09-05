import os
import requests
import json
import time
import pymysql
import uuid
import math
import minimalmodbus

from datetime import datetime

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='PLC',
    password='123123123',
    db='graphiccontrol'
)
db.autocommit = True


class RS485:
    def __init__(self, port, SlaveAddress):
        self.minimalmodbus = minimalmodbus.Instrument(port=port, slaveaddress=SlaveAddress)
        self.minimalmodbus.serial.baudrate = 9600
        self.minimalmodbus.serial.bytesize = 7
        self.minimalmodbus.serial.parity = 'E'
        self.minimalmodbus.serial.stopbits = 1
        self.minimalmodbus.serial.timeout = 1
        self.minimalmodbus.mode = minimalmodbus.MODE_ASCII
        self.minimalmodbus.clear_buffers_before_each_transaction = True
        self.minimalmodbus.close_port_after_each_call = True

    def Read_Bit(self, TmpAddress):
        return self.minimalmodbus.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)

    def Write_Bit(self, TmpAddress, TmpBool):
        return self.minimalmodbus.write_bit(registeraddress=int(TmpAddress, 16), value=TmpBool, functioncode=5)

    def Read_Register(self, TmpAddress):
        return self.minimalmodbus.read_register(
            registeraddress=int(TmpAddress, 16),
            number_of_decimals=0,
            functioncode=3,
            signed=True
        )

    def Write_Register(self, TmpAddress, TmpValue):
        return self.minimalmodbus.write_register(
            registeraddress=int(TmpAddress, 16),
            value=TmpValue,
            number_of_decimals=0,  # 1 2 3 4
            functioncode=16,
            signed=True
        )


TmpRS485 = RS485('COM5', 1)
with db.cursor() as cursor:
    # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
    command = "SELECT*FROM `chart_collects`"
    cursor.execute(command)
    db.commit()
    tmp1 = cursor.fetchall()
    for n in tmp1:
        print(n)
    command = "SELECT*FROM `v_words`"
    cursor.execute(command)
    db.commit()
    tmp2 = cursor.fetchall()
    for m in tmp2:
        print(m)