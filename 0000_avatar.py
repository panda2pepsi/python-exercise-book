# -*-coding:utf-8-*-

# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字
# 类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

img_path = "E:\\Codes\\Python\\Internet_Projects\\Exercise Book\\source\\0000_2.jpg"
img01 = Image.open(img_path)
width, height = img01.size
text_size = int(width / 5)
text_font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", text_size)
draw_img01 = ImageDraw.Draw(img01)
draw_img01.text((width * 0.8, height * 0.06), "1", "red", font=text_font)
img01.show()