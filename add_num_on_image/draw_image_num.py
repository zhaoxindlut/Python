#coding:utf-8
#!/usr/bim/python
#采用Python事实上的标准图像处理库PIL
#关于PIL的简单教程见http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000

'''在图片右上角加上红色的数字，类似于微信未读信息数量那种提示效果。'''

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-50, 5), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('1.jpg')
    add_num(image)