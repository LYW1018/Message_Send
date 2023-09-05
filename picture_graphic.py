# import os
# import requests
# import json
# import time
# import pymysql
# import uuid
# import math
# import minimalmodbus
#
# from datetime import datetime
#
# db = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='PLC',
#     password='123123123',
#     db='graphiccontrol'
# )
# db.autocommit = True
#
#
# class RS485:
#     def __init__(self, port, SlaveAddress):
#         self.minimalmodbus = minimalmodbus.Instrument(port=port, slaveaddress=SlaveAddress)
#         self.minimalmodbus.serial.baudrate = 9600
#         self.minimalmodbus.serial.bytesize = 7
#         self.minimalmodbus.serial.parity = 'E'
#         self.minimalmodbus.serial.stopbits = 1
#         self.minimalmodbus.serial.timeout = 1
#         self.minimalmodbus.mode = minimalmodbus.MODE_ASCII
#         self.minimalmodbus.clear_buffers_before_each_transaction = True
#         self.minimalmodbus.close_port_after_each_call = True
#
#     def Read_Bit(self, TmpAddress):
#         return self.minimalmodbus.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#     def Write_Bit(self, TmpAddress, TmpBool):
#         return self.minimalmodbus.write_bit(registeraddress=int(TmpAddress, 16), value=TmpBool, functioncode=5)
#
#     def Read_Register(self, TmpAddress):
#         return self.minimalmodbus.read_register(
#             registeraddress=int(TmpAddress, 16),
#             number_of_decimals=0,
#             functioncode=3,
#             signed=True
#         )
#
#     def Write_Register(self, TmpAddress, TmpValue):
#         return self.minimalmodbus.write_register(
#             registeraddress=int(TmpAddress, 16),
#             value=TmpValue,
#             number_of_decimals=0,  # 1 2 3 4
#             functioncode=16,
#             signed=True
#         )
#
#
# TmpRS485 = RS485('COM5', 1)
# with db.cursor() as cursor:
#     command = "SELECT*FROM `v_words`"
#     cursor.execute(command)
#     db.commit()
#     tmp1 = cursor.fetchall()
#     for m in tmp1:
#         Int_TimeStamp = int(time.time())
#         TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#         # print(m)
#     command = "SELECT*FROM `chart_collects`"
#     cursor.execute(command)
#     db.commit()
#     tmp2 = cursor.fetchall()
#     B = {}
#     C = []
#     for n in tmp2:
#         Int_TimeStamp = int(time.time())
#         TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#         # print(n)
#         A = n[1].split(',')
#         # print(A)
#         for v in A:
#             C.append(v)
#
#             # B[C]={n[2],n[3]}
#             D = json.dumps(C)
#             print(D)
#             for w in D:
#                 B[D]={n[0],n[2],n[3]}
#     print(B)



import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus
import requests
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

message = MIMEMultipart()

db_settings = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'PLC',
    "password": '123123123',
    "db": "graphiccontrol",
    "charset": "utf8"
}

con = pymysql.connect(**db_settings)
con.autocommit = True

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
            number_of_decimals=0,  # 1 2 3 4
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


def Show(avg1, avg2, avg3):
    print('{} {} {}'.format(avg1, avg2, avg3))


TmpRS485 = RS485('COM5', 1)
while con.open:
    ChartValue = {}
    with con.cursor() as cursor:
        command = "SELECT * FROM `v_words`"
        cursor.execute(command)
        con.commit()
        vals = cursor.fetchall()
        for n in vals:
            TmpNotifyCollect = json.loads(n[8])
            TmpRegisterValue = TmpRS485.Read_Register(TmpAddress=n[2])
            ChartValue[n[2]] = {
                'Guid': n[0], 'Name': n[1], 'Address': n[3],
                'Value': int(TmpRegisterValue), 'Type': 'Word'
            }

        command = "SELECT * FROM `chart_collects`"
        cursor.execute(command)
        con.commit()
        for key1, value1 in enumerate(cursor.fetchall()):
            TmpOccurTimeStamp = int(time.time())
            TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
            TmpGuid = value1[0]
            TmpAddress = value1[1]

            NewChartValue = {}
            for key2, value2 in enumerate(TmpAddress.split(',')):
                NewChartValue[value2] = {
                    'Name': ChartValue[value2]['Name'],
                    'Address': ChartValue[value2]['Address'],
                    'Value': 0,
                }
                if not ChartValue.get(value2) is None:
                    NewChartValue[value2] = {
                        'Name': ChartValue[value2]['Name'],
                        'Address': ChartValue[value2]['Address'],
                        'Value': ChartValue[value2]['Value'],
                    }
            command = "INSERT INTO `chart_values`(`Guid`, `ChartCollectsGuid`, `TimeStamp`, `Collect`, `created_at`, `updated_at`)VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(command, (str(uuid.uuid4()), TmpGuid, TmpOccurTimeStamp, json.dumps(NewChartValue), TmpOccurDate, TmpOccurDate))
            con.commit()
    print('Running... {}'.format(TmpOccurDate))
exit(0)
