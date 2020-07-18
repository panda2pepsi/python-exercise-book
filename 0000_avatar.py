from PIL import Image, ImageDraw, ImageFont

img_path = "E:\\Codes\\Python\\Internet_Projects\\Exercise Book\\source\\0000_2.jpg"
# open image
img01 = Image.open(img_path)
# get the img width and height
width, height = img01.size
# set the font size, based on the image size
text_size = int(width / 5)
# set the text font
text_font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", text_size)
# start to draw sth on it
draw_img01 = ImageDraw.Draw(img01)
# add text on this image
draw_img01.text((width * 0.8, height * 0.06), "1", "red", font=text_font)
# call the image viewer
img01.show()