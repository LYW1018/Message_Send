import uuid

import pymysql
import uuid  # 寫入 Guid 唯一碼
from datetime import datetime

db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='graphiccontrol'
)
db.autocommit = True
#
# tmp = []
# tmp1 = 5
# for n in range(5):
#     tmp.append([str(uuid.uuid4()), tmp1 * n, tmp1 * n + 1, tmp1 * n + 2, tmp1 * n + 3,int(n)])
#     tmp1 += 1

# ---------------------------------------------------------------------
# 新建檔案於SQL上
# with db.cursor() as cursor:
#     sql = '''CREATE TABLE `graphiccontrol`.`User` (
# 	    `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	    `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	    `Age` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	    `Postal_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	    `City_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	    PRIMARY KEY (`Guid`),
# 	    INDEX (`Name`),
# 	    INDEX (`Age`),
# 	    UNIQUE (`Postal_Guid`),
# 	    UNIQUE (`City_Guid`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci'''
#     cursor.execute(sql)
#     db.close()
# ---------------------------------------------------------------------
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
# ---------------------------------------------------------------------
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
# ---------------------------------------------------------------------
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
# with db.cursor() as cursor:
#     sql= '''CREATE TABLE `graphiccontrol`.`ITOrder` (
# 	    `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
# 	    `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
# 	    `Price` INT UNSIGNED NOT NULL COMMENT '價錢',
# 	    `weight` INT UNSIGNED NOT NULL COMMENT '重量',
# 	    PRIMARY KEY (`Guid`),
# 	    INDEX (`Name`),
# 	    INDEX (`Price`),
# 	    INDEX (`weight`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;'''
# ---------------------------------------------------------------------
# tmp = []
# TmpI = 5
# for n in range(5):
#     tmp.append([str(uuid.uuid4()), 'A', n * 5 + 1, n * 5 + 2])
#     TmpI += 1
#
# with db.cursor() as cursor:
#     SQL = "INSERT INTO `ITOrder` (`Guid`, `Name`,`Price`,`weight`) values (%s, %s , %s, %s)"
#     for n in tmp:
#         cursor.execute(SQL, (n[0], n[1], int(n[2]), int(n[3])))
#         db.commit()
# ---------------------------------------------------------------------
# with db.cursor() as cursor:
#     # SQL = "select * from `ITOrder` order by Price desc"
#     SQL = "select * from `ITOrder` where Price < 15 order by Price desc"
#     cursor.execute(SQL)
#     TmpX = cursor.fetchall()
#     for n in TmpX:
#         print(n)
# exit(0)
# ---------------------------------------------------------------------
# 更新update-型態01
# with db.cursor() as cursor:
#     command = "UPDATE `user` SET `Name`='H2' where `Guid`='a';"
#     cursor.execute(command)
#     db.commit()
#     db.close()
# ---------------------------------------------------------------------
# 更新update-型態02
# with db.cursor() as cursor:
#     command = "UPDATE `user` SET `Name`='H3' where `Guid`=%s"
#     cursor.execute(command, 'b')
#     db.commit()
#     db.close()
# ---------------------------------------------------------------------
# SQL刪除指令(Delete)
# with db.cursor() as cursor:
#     command="DELETE FROM `user` where `Guid`=%s"
#     cursor.execute(command,'c')
#     db.commit()
#     db.close()


#####################################################################################################
# 資料表新增(bit_cells)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`bit_cells` (
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()
# # TIMESTAMP是時間每秒計算更新
# # 若是即時更新就需導入此條件
#Time
# import time
# print(time.time())
# Int_TimeStamp = int(time.time())
# print(datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%D %H:%M:%S'))

# import time
#
# Int_TimeStamp = int(time.time())
# TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#
#
# with db.cursor() as cursor:
#     SQL = """
#         INSERT INTO `bit_cells`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,0,99,99,'{}',0,
#             '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#             %s,%s
#         );
#     """
#     for n in [
#         ['M0', '800'], ['M1', '801'], ['M2', '802'], ['M3', '803'], ['M4', '804']
#         , ['M5', '805'], ['M6', '806'], ['Y0', '500'], ['Y1', '501'], ['Y2', '502']
#         , ['Y3', '503'], ['Y4', '504'], ['Y5', '505'], ['Y6', '506'], ['Y7', '507']
#         , ['Y10', '508'], ['Y11', '509'], ['Y12', '50A']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()


#####################################################################################################
# 資料表新增(v_strings)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`v_strings` (
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()

# import time
#
# Int_TimeStamp = int(time.time())
# TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')

#
# with db.cursor() as cursor:
#     SQL = """
#          INSERT INTO `v_strings`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"String\",\"SignedType\":true,\"NumberOfRegisters\":1,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,'{\"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2006', '17D6'], ['D2007', '17D7'], ['D2008', '17D8'], ['D2009', '17D9'], ['D2010', '17DA']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()
#####################################################################################################
# 資料表新增(v_words)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`v_words` (
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()

# with db.cursor() as cursor:
#     SQL = """
#         INSERT INTO `v_words`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"Word\",\"SignedType\":true,\"NumberOfDecimals\":0,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,
#             '{\"NotifyPlatFrom\": 2, \"NotifyTimeStamp\": 1685327881, \"NotifyDateTime\": \"2023-05-29 10:38:01\"}',
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2000', '17D0'], ['D2001', '17D1'], ['D2002', '17D2'], ['D2004', '17D4'],
#         ['D2021', '17E5'], ['D2022', '17E6'], ['D2023', '17E7'], ['D2024', '17E8'], ['D2025', '17E9']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()
#####################################################################################################
# 資料表新增(chart_collects)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`chart_collects` (
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址集合',
#     `Data` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '參數集合',
#     `Remark` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '備注',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40))
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()
# with db.cursor() as cursor:
#     sql='''INSERT INTO `chart_collects`(`Guid`,`Address`,`Data`,`Collect`,`Remark`,`created_at`,`updated_at`)
#         VALUES ('130e6ad1-6d02-4b95-a9dc-3413ebe47919','17E8,17E9', '{}', '{}', '折線圖', '2023-05-17 01:47:39', '2023-05-29 03:06:54'),
#                 ('eb0f27a7-1384-4ad4-a0c1-230dcf93b8df','17E5,17E6,17E7', '{}', '{}', '圓餅圖','2023-05-17 02:27:32', '2023-05-17 02:27:32');'''
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         db.rollback()
#         db.close()

#####################################################################################################
# # 資料表新增(chart_values)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`chart_values` (
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `ChartCollectsGuid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '圖表設定唯一碼',
#     `TimeStamp` INT UNSIGNED NOT NULL COMMENT '當下秒數',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`ChartCollectsGuid`(40)),
#     INDEX (`TimeStamp`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()
#####################################################################################################
# 資料表新增(settings)
# with db.cursor() as cursor:
#     sql = """CREATE TABLE `graphiccontrol`.`settings` (
#     `Guid` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '全局唯一識別元',
#     `Name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `CollectData` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40))
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;"""
#     cursor.execute(sql)
#     db.close()
# with db.cursor() as cursor:
#     sql='''INSERT INTO `settings`(`Guid`, `Name`, `CollectData`, `created_at`, `updated_at`)
#         VALUES ('427841f6-a5b5-4658-a4d7-105a5730124c', 'LoopTimes','{\"ReTry\":3,\"LineNotifyLimitTime\":60}', '2023-05-16 05:28:18', '2023-05-2904:28:28'),
#                 ('4605e414-192f-4667-82d1-fcbd2766255f', 'SMS','{\"OwnPhone\":\"0972153032\",\"OwnPassword\":\"~!QAZ2wsx\",\"Group\":[{\"Phone\":\"0972153032\"}]}', '2023-05-16 05:28:18', '2023-05-31 02:02:10'),
#                 ('4650c0d7-ae99-40f0-9572-a3375c03e68d', 'Line','{\"Group\":[{\"Token\":\"1FP4CFtj7O7cCX59jAfdLiu8GCqOu6Xe26Kd2v5ZgYk\"}]}','2023-05-16 05:28:18', '2023-05-29 04:24:36'),
#                 ('e972137f-347a-41c7-b662-9a378de35211', 'Email','{\"OwnEmail\":\"nexstar1436@gmail.com\",\"OwnPassword\":\"pzhuiybsqjrbbdgk\",\"Group\":[{\"ToEmail\":\"nexstar1436@gmail.com\"}]}', '2023-05-16 05:28:18','2023-05-31 02:05:47');
#                 '''
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         db.rollback()
#         db.close()
#####################################################################################################
# 半成品
# tmp = []
# tmp1 = ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6',
#         'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11','Y12']
# tmp2 =['800','801','802','803','804','805','806','500','501','502','503','504','505','506','507','508','509','50A']
# for n in range(18):
#     tmp.append([str(uuid.uuid4()), tmp1, tmp2, tmp1 * n + 2, tmp1 * n + 3, int(n)])
#
# with db.cursor() as cursor:
#     sql = '''INSERT INTO `bit_cells`(
#     `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,
#     `HandTriggerValue`,`CollectData`,`NotifyStatus`,
#     `NotifyCollectData`,`created_at`,`updated_at`)
#     VALUES (%s,%s,%s,%s,%s);'''
#     try:
#         for n in tmp:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3], n[4]))  # 執行
#             db.commit()  # 下確定後寫入
#     except:
#         db.rollback()
#     db.close()
#####################################################################################################
