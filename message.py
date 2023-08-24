# 金鑰 1 (圖空專班)：rJVudIUQvCiRY3qpDbGIoe7KqRC032dvXcTQBdKyQ30
# 金鑰 2 (圖控專用line訊息接收)：VmYTOq4sCGn128jn1xPjCcArVt9HYitoSsQ2eUgHE7h
import requests
import json
Message = 'system did not responce, Error'  # 輸入文字敘述
LineToken = 'VmYTOq4sCGn128jn1xPjCcArVt9HYitoSsQ2eUgHE7h'  # 金鑰輸入
Tmp = requests.post('https://notify-api.line.me/api/notify',
                    params={'message': Message},
                    headers={'Authorization': 'Bearer ' + LineToken,
                             'Content-Type': 'application/x-www-form-urlencoded'})  # 為一規則
# print(type(Tmp.text))
# print(type(Tmp.content))


# print(Tmp.text)
# print(type(Tmp.text))
# print(json.loads(Tmp.text))
# print(type(json.loads(Tmp.text)))
# print(json.loads(Tmp.text)['status'])
