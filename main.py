import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 文字圖片統一歸納
from email.mime.application import MIMEApplication
from email.header import Header

message = MIMEMultipart()  # 協助包裝元素


def UploadFileToByte(Path, Name):
    with open('{}/{}'.format(Path, Name), 'rb') as file:
        part = MIMEApplication(file.read(), Name=Name)  # 檔案上傳
        part['Content-Dispostion'] = 'attachment; filename={name}'.format(name=Name)  # 資料名稱定義
    return part


message['Subject'] = Header('Subject', 'utf-8')  # 撰寫郵件標題
message['From'] = Header('YW', 'utf-8')  # 寄件者(名稱或別名)
message['To'] = Header('MH', 'utf-8')  # 收件者(名稱或別名)
# message['Cc']='m10803126@gapps.ntust.edu.tw,t10830b609@ntut.org.tw,'#副本收件人1,2

# 文字呈現
message.attach(MIMEText('打LOL阿', 'plain', 'utf-8'))
# 第一格:資料來源
# 第二格:資料來源類型
# 第三格:格式

# 網頁呈現
TestHtml = '''
<!DOCTYPE html>
<html>
<body>

<h2>HTML Table</h2>

<h2>Absolute URLs</h2>
<p><a href="https://www.w3.org/">W3C</a></p>
<p><a href="https://www.google.com/">Google</a></p>

<h2>Relative URLs</h2>
<p><a href="html_images.asp">HTML Images</a></p>
<p><a href="/css/default.asp">CSS Tutorial</a></p>

<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
  Sorry, your browser does not support inline SVG.
</svg>

<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 million globally.
</blockquote>


<table style="font-family: arial, sans-serif;border-collapse: collapse;width: 100%;">
  <tr>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Company</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Contact</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Country</th>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Alfreds Futterkiste</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><span style="font-size:100px">🐰🤞🤖👽🕜🕝🀄🔞</span></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Germany</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Centro comercial Moctezuma</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Francisco Chang</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Mexico</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Ernst Handel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Roland Mendel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Austria</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Island Trading</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Helen Bennett</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">UK</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Laughing Bacchus Winecellars</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Yoshi Tannamuri</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Canada</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Magazzini Alimentari Riuniti</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><img src="https://www.w3schools.com/html/img_girl.jpg" alt="Girl in a jacket" style="width:100%;height:500px;"></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Italy</td>
  </tr>
</table>

</body>
</html>
'''
message.attach(MIMEText(TestHtml,'html','utf-8'))
# 第一格:資料來源
# 第二格:資料來源類型
# 第三格:格式

# 附件檔案
Array = [['MOVIE', 'AAAA.pdf'], ['MOVIE', 'AAAAA.mp4'], ['MOVIE', 'AGA.mp4']]
for n in range(0, len(Array)):
    message.attach(UploadFileToByte(Array[n][0], Array[n][1]))

msg = message.as_string()  # 將msg將text轉換成str
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('m10803126@gapps.ntust.edu.tw', 'cneuuddkdfiwohrx')
from_addr = 'm10803126@gapps.ntust.edu.tw'
to_addr = 't10830b609@ntut.org.tw'
status = smtp.sendmail(from_addr, to_addr, msg)
# 加密文件，避免私密訊息被截取
DoneSatus = False
if status == {}:
    DoneSatus = True
smtp.quit()
print(DoneSatus)
