import requests

# 發送指令
# Ur1 = 'https://{DoMain}/API21/SendSMS.ashx'.format(DoMain='api.e8d.tw')
# tmp = requests.post(Url, data={
#     'UID': '0972153032',#帳號
#     'PWD': '~!QAZ2wsx',#密碼
#     'SB': '',
#     'MSG': 'ABC'.encode('utf-8'),#輸入簡訊內容
#     'DEST': '0952717700',#輸入接收者電話號碼
#     'ST': '',
#     'RETRYTIME': 1440
# }, headers={}, timeout=5)
# print(tmp.text)

# 發送狀態查詢
# Url = 'https://{DoMain}/API21/HTTP/GetDeliveryStatus.ashx'.format(DoMain='api.e8d.tw')
# tmp = requests.post(Url, data={
#     'UID': '0972153032',
#     'PWD': '~!QAZ2wsx',
#     'BID': '6a8c8ad1-f7c3-42e9-80b1-2f605ff56cc6',
#     'PNO': 1,
#     'RESPFORMAT': 1
# }, headers={}, timeout=5)
# print(tmp.text)

# 餘額查詢
Url = 'https://{DoMain}/API21/HTTP/GetCredit.ashx'.format(DoMain='api.e8d.tw')
tmp = requests.post(Url, data={
    'UID': '0972153032',
    'PWD': '~!QAZ2wsx',
}, headers={}, timeout=5)
print(tmp.text)
