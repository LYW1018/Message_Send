import uuid

import pymysql
import uuid  # 寫入 Guid 唯一碼

db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='graphiccontrol'
)
# db.autocommit = True
#
# tmp = []
# tmp1 = 5
# for n in range(5):
#     tmp.append([str(uuid.uuid4()), tmp1 * n, tmp1 * n + 1, tmp1 * n + 2, tmp1 * n + 3,int(n)])
#     tmp1 += 1


# 新建檔案於SQL上
with db.cursor() as cursor:
    sql = '''CREATE TABLE `graphiccontrol`.`User` (
	    `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
	    `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
	    `Age` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
	    `Postal_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
	    `City_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
	    `series`int CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
	    PRIMARY KEY (`Guid`),
	    INDEX (`Name`),
	    INDEX (`Age`),
	    UNSIGNED (`序列`)
	    UNIQUE (`Postal_Guid`),
	    UNIQUE (`City_Guid`)
    ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci'''
    cursor.execute(sql)
    db.close()

# 建立資料內容(單筆新增)
# with db.cursor() as cursor:
#     sql='''INSERT INTO `User`(`Guid`,`Name`,`Age`,`Postal_Guid`,`City_Guid`)
#         VALUES ('5cf504a2-da34-42f9-9cfd-ec59a3755aab','A1','15','0e9d1192-3d2b-4c22-8627-e9fcb11c4115','1839f963-e859-402b-9ebc-46e5f969767f');'''
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         db.rollback()
#         db.close()

# 多筆資料寫入SQL
# A = ['a', 'a1', 'a2', 'a3', 'a4']
# B = ['b', 'b1', 'b2', 'b3', 'b4']
# C = ['c', 'c1', 'c2', 'c3', 'c4']
# with db.cursor() as cursor:
#     sql = '''INSERT INTO `User`(`Guid`,`Name`,`Age`,`Postal_Guid`,`City_Guid`)
#         VALUES (%s,%s,%s,%s,%s);'''
#     try:
#         for n in [A, B, C]:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3], n[4]))  # 執行
#             db.commit()  # 下確定後寫入
#     except:
#         db.rollback()
#     db.close()
# __________________________________________________________________________________________

# with db.cursor() as cursor:
#     sql = '''INSERT INTO `User`(`Guid`,`Name`,`Age`,`Postal_Guid`,`City_Guid`)
#         VALUES (%s,%s,%s,%s,%s);'''
#     try:
#         for n in tmp:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3], n[4]))  # 執行
#             db.commit()  # 下確定後寫入
#     except:
#         db.rollback()
#     db.close()

# 從SQL取回一筆數值(多筆數據)
# with db.cursor() as cursor:
#     # command = 'SELECT*FROM `User` order by Age DESC'  # 單筆數據排列
#     command = 'SELECT*FROM `User` order by `Age` DESC'
#     cursor.execute(command)
#     db.commit()
#     for m in cursor.fetchall():
#         print(m)
#     # vals = cursor.fetchone()
#     # print(vals)
#     db.close()
