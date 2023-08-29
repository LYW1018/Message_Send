import csv

data = [['Name', 'Age', 'Location'],
        ['John', '25', 'New York'],
        ['Jane', '30', 'Los Angeless']
        ]
path = 'output.csv'

# # write
# with open(path, 'w', newline='') as file:  # with 的用意是可減少多一行程式碼
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
# # Read
# with open(path, 'r') as file:
#     csv_readwer = csv.reader(file)
#     for row in csv_readwer:
#         print(row)
with open('output1.csv', 'a', encoding='utf-8-sig') as file:
    file.write('姓名, 年齡, 地點')
    file.write('\nYW,27,ABC')
