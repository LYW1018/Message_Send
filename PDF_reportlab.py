from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics  # 新增字體
from reportlab.pdfbase.ttfonts import TTFont

# 創建一個PDF文件
c = canvas.Canvas('Test.pdf', pagesize=letter)

pdfmetrics.registerFont(TTFont('kaiu', 'kaiu.ttf'))
# 增加文本
c.setFont('kaiu', 14)
c.drawString(100, 750, '下課')
# A.encode('unicode_escape')

# 增加圖形
c.setStrokeColorRGB(1, 0, 0)  # 設定邊框顏色
c.rect(50, 650, 400, 100, fill=0)  # 繪製矩形

# 保存PDF文件
c.showPage()
c.save()
