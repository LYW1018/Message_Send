import json

import pymysql
import uuid  # 寫入 Guid 唯一碼
from datetime import datetime

db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='graphiccontrol'
)
db.autocommit = True

# 從SQL取回一筆數值(多筆數據)
with db.cursor() as cursor:
    # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
    command = "SELECT*FROM `bit_cells`"
    cursor.execute(command)
    db.commit()
    tmp = cursor.fetchall()

    # 成品
    A = []
    for m in tmp:  # 把所需資料拉出來
        if m[1] == 'M5':
            A.append(m)
    for n in A:  # 將陣列中的第八項拉出判別，若==1,則將第八項的字串轉換成字典,設變數將字典中的NT及NP數值拉出
        if n[7] == 1:
            B = json.loads(n[8])  # 字串轉成字典
            NotifyT = int(B['NotifyType'])
            NotifyP = int(B['NotifyPlatFrom'])
            if NotifyT == 1 and NotifyP == 2:  # 設條件啟動
                print('line on')
    # 另解

    for m in tmp:
        if m[1] == 'M5' and m[7] == 1:
            B = json.loads(m[8])
            NotifyT = int(B['NotifyType'])
            NotifyP = int(B['NotifyPlatFrom'])
            if NotifyT ==' 1' and NotifyP == '2':
                print('line on')

    # vals = cursor.fetchone()
    # print(vals)
    db.close()
