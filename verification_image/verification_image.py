#coding:utf-8
#!/usr/bin/python
#利用PIL库生成随机的验证图片

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

#生成随机字母
#ascii中，32～126(共95个)是字符(32是空格），其中48～57为0到9十个阿拉伯数字。
#65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等。
def rand_char():
    return chr(random.randint(65,90))

#随机颜色，用于背景
def randColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

#随机颜色2，用于字体
def randColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

#设置图片尺寸
def setsize(width, height):
    return width,height


width = 60 * 4
height = 60

#创建新的图片对象
image = Image.new('RGB', (width,height), (255,255,255))

#创建字体对象，不同平台需要修改为对应字体文件的路径
font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size = 50)

#创建draw对象，对图片对象的编辑过程需要通过draw对象来完成
draw = ImageDraw.Draw(image)

#使用随机颜色1填充图片的每一个像素
#draw.point(点坐标，颜色)填充单个像素点
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = randColor())  

#在图片上输出文字
#draw.text(位置，写入字符，font=字体，fill=颜色)。。
for i in range(4):
    draw.text((60*i+10, 10), rand_char(), font=font, fill=randColor2()) 

#添加模糊特效
image = image.filter(ImageFilter.BLUR)
image.save('verification.jpg', 'jpeg')