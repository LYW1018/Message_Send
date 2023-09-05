import json

# import pymysql
# import uuid  # 寫入 Guid 唯一碼
# from datetime import datetime

# db = pymysql.connect(
#     host='127.0.0.1', port=3306,
#     user='PLC', password='123123123',
#     db='graphiccontrol'
# )
# db.autocommit = True

# 從SQL取回一筆數值(多筆數據)
# with db.cursor() as cursor:
#     # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
#     command = "SELECT*FROM `bit_cells`"
#     cursor.execute(command)
#     db.commit()
#     tmp = cursor.fetchall()
#
#     # 成品
#     A = []
#     for m in tmp:  # 把所需資料拉出來
#         if m[1] == 'M5':
#             A.append(m)
#     for n in A:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
#         if n[7] == 1:
#             B = json.loads(n[8])  # 字串轉成字典
#             NotifyT = int(B['NotifyType'])
#             NotifyP = int(B['NotifyPlatFrom'])
#             if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
#                 print('line on')
#     # 另解
#
#     for m in tmp:
#         if m[1] == 'M5' and m[7] == 1:
#             B = json.loads(m[8])
#             NotifyT = int(B['NotifyType'])
#             NotifyP = int(B['NotifyPlatFrom'])
#             if NotifyT ==' 1' and NotifyP == '2':
#                 print('line')
#
#     # vals = cursor.fetchone()
#     # print(vals)
#     db.close()
# ***********************************************************************************************************

# 即時更新檔案

import time
from datetime import datetime

# Int_TimeStamp = int(time.time())
# TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')

# while True:
#     with db.cursor() as cursor:
#         # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
#         command = "SELECT*FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         tmp = cursor.fetchall()
#     for n in tmp:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
#         Int_TimeStamp = int(time.time())
#         TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#         if n[7] != 1:
#             continue
#         if n[7] == 1:
#             B = json.loads(n[8])  # 字串轉成字典
#             NotifyT = int(B['NotifyType'])
#             NotifyP = int(B['NotifyPlatFrom'])
#             if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
#                 print(n[1], 'line ON', TmpDate)
#             elif NotifyT == 1 and NotifyP == 1:
#                 print(n[1], 'Email ON', TmpDate)
#             elif NotifyT == 1 and NotifyP == 0:
#                 print(n[1], 'SMS ON', TmpDate)
#             time.sleep(1)


# *************************************************************************************************
# print('RS232_485')
import minimalmodbus

# 即時更新檔案

# import time
# from datetime import datetime
#
# def minimalmodbus()
#
# Int_TimeStamp = int(time.time())
# TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#
# while True:
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     # c.mode=minimalmodbus.MODE_RTU
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     start_time = time.time()
#
#     # TmpY = c.read_bits(
#     #     registeraddress=int('500', 16),
#     #     number_of_bits=6,
#     #     functioncode=2
#     # )
#     # print(TmpY)
#     #
#     # TmpM = c.read_bits(
#     #     registeraddress=int('800', 16),
#     #     number_of_bits=6,
#     #     functioncode=2
#     # )
#     # print(TmpM)
#
#     with db.cursor() as cursor:
#         # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
#         command = "SELECT*FROM `bit_cells`"
#         cursor.execute(command,)
#         db.commit()
#         tmp = cursor.fetchall()
#
#         for n in tmp:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
#             Int_TimeStamp = int(time.time())
#             TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#
#             sql = """
#                         UPDATE `bit_cells` SET `NowValue`=%s where `Name`= n[1]"""
#             cursor.execute(command, )
#             db.commit()
#
#             if n[7] != 1:
#                 continue
#             if n[7] == 1:
#                 B = json.loads(n[8])  # 字串轉成字典
#                 NotifyT = int(B['NotifyType'])
#                 NotifyP = int(B['NotifyPlatFrom'])
#                 if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
#                     print(n[1], 'line ON', TmpDate)
#                 elif NotifyT == 1 and NotifyP == 1:
#                     print(n[1], 'Email ON', TmpDate)
#                 elif NotifyT == 1 and NotifyP == 0:
#                     print(n[1], 'SMS ON', TmpDate)
#                 time.sleep(1)
# *************************************************************************************************
# import os
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
#
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))
#
#
# def RS485_read(TmpAddress):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             command = "UPDATE `bit_cells` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (RS485_read(n[2]), TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
#     time.sleep(1)
# exit(0)


# *************************************************************************************************
# import os
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
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))
#
#
# def RS485_write(TmpAddress, OnOFF):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.write_bit(registeraddress=int(TmpAddress, 16), value=OnOFF, functioncode=5)
#
#
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             if n[4] != 1:
#                 continue
#             if n[5] == 99:
#                 continue
#             RS485_write(n[2], n[5])
#             command = "UPDATE `bit_cells` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
#             cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
#             db.commit()
#     time.sleep(1)
#     print('Running... {}'.format(TmpOccurDate))
# exit(0)

# *************************************************************************************************

# import os
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
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))
#
#
# def RS485_write(TmpAddress, OnOFF):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.write_bit(registeraddress=int(TmpAddress, 16), value=OnOFF, functioncode=5)
#
#
# def RS485_read(TmpAddress):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         # A = []
#         # for m in vals:  # 把所需資料拉出來
#         #     if m[1] == 'M5':
#         #         A.append(m)
#         # for n in A:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
#         #     if n[7] == 1:
#         #         B = json.loads(n[8])  # 字串轉成字典
#         #         NotifyT = int(B['NotifyType'])
#         #         NotifyP = int(B['NotifyPlatFrom'])
#         #         if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
#         #             print('line on')
#
#         for n in vals:
#             command = "UPDATE `bit_cells` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (RS485_read(n[2]), TmpOccurDate, n[0]))
#
#         for n in vals:
#             if n[4] != 1:
#                 continue
#             if n[5] == 99:
#                 continue
#             RS485_write(n[2], n[5])
#             command = "UPDATE `bit_cells` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
#             cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
#             db.commit()
#
#     print('Running... {}'.format(TmpOccurDate))
# exit(0)
# *************************************************************************************************

import os
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


#
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))


# def RS485_write(TmpAddress, OnOFF):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.write_bit(registeraddress=int(TmpAddress, 16), value=OnOFF, functioncode=5)


# def RS485_read(TmpAddress):
#     c = minimalmodbus.Instrument(port='COM5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `v_words`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#
#         # for n in vals:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
#         #     if n[7] == 1:
#         #         B = json.loads(n[8])  # 字串轉成字典
#         #         NotifyT = int(B['NotifyType'])
#         #         NotifyP = int(B['NotifyPlatFrom'])
#         #         if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
#         #             print('line on')
#
#         for n in vals:
#             command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (RS485_read(n[2]), TmpOccurDate, n[0]))
#
#         # for n in vals:
#         #     if n[4] != 1:
#         #         continue
#         #     if n[5] == 99:
#         #         continue
#         #     RS485_write(n[2], n[5])
#         #     command = "UPDATE `v_words` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
#         #     cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
#         #     db.commit()
#
#     print('Running... {}'.format(TmpOccurDate))
# exit(0)
#
# *************************************************************************************************
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
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))
#
#
# TmpRS485 = RS485('COM5', 1)
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `v_words`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             # Read
#             command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (TmpRS485.Read_Register(TmpAddress=n[2]), TmpOccurDate, n[0]))
#             db.commit()
#         for n in vals:
#             if n[4] != 1:
#                 continue
#             if n[5] == 99:
#                 continue
#             TmpRS485.Write_Register(TmpAddress=n[2], TmpValue=int(n[5]))
#             command = "UPDATE `v_words` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
#             cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
# exit(0)
# *************************************************************************************************
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


# while True:
with db.cursor() as cursor:
    # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
    command = "SELECT*FROM `bit_cells`"
    cursor.execute(command)
    db.commit()
    tmp = cursor.fetchall()
    for n in tmp:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
        Int_TimeStamp = int(time.time())
        TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        if n[7] != 1:
            continue
        if n[7] == 1:
            # print(n)
            B = json.loads(n[8])  # 字串轉成字典
            NotifyT = int(B['NotifyType'])
            NotifyP = int(B['NotifyPlatFrom'])
            NotifyTSPS = 'NotifyTimeStamp'
            NotifyDT = 'NotifyDateTime'
            # print(B)
            if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
                # print(n)
                T1 = datetime.fromtimestamp(Int_TimeStamp).strftime('%S')
                T2 = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
                B[NotifyTSPS] = T1
                B[NotifyDT] = T2
                C = json.dumps(B)
                command = "UPDATE `bit_cells` SET `NotifyCollectData`=%s where `Guid`=%s"
                cursor.execute(command, (C, n[0]))
                db.commit()

        #     elif NotifyT == 1 and NotifyP == 1:
        #         print(n[1], 'Email ON', TmpDate)
        #     elif NotifyT == 1 and NotifyP == 0:
        #         print(n[1], 'SMS ON', TmpDate)
        #     time.sleep(1)
