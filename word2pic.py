from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import random


def translate(txt):
    # 画饼 这里要支持简单 markdown
    # to be done
    f = open(txt, 'r', encoding='utf-8')
    string = f.read()
    f.close()
    return string


def word2pic(txt, ttf, save, font_x, bg_image, dis_x, dis_y):
    # 源文件 字体 保存路径 一行显示字体个数 背景图片 页边距横向 页边距纵向
    img = Image.open(bg_image)
    img_wid, img_height = img.size

    font_size = (img_wid-dis_x*2)//(font_x)+7
    font_y = (img_height-dis_y*2)//(font_size)  # 竖行字体个数计算

    font = ImageFont.truetype(ttf, font_size)  # 设置字体

    string = translate(txt)
    length = len(string)

    page = 1
    iter = 0
    while iter < length:
        img = Image.open(bg_image)
        draw = ImageDraw.Draw(img)
        for i in range(font_y):
            for j in range(font_x):
                if(iter >= length):
                    break
                if string[iter] == '\n':
                    iter += 1
                    break
                draw.text((dis_x+(font_size-7)*j+random.uniform(-3, 3), dis_y+(font_size)*i+random.uniform(-3, 3)), string[iter], (0, 0, 0), font=font)
                iter += 1
        img.save(save + str(page) + ".png", dpi=(150.0, 150.0))
        page += 1
    return page


if __name__ == "__main__":
    txt_path = './src/test.txt'
    ttf_path = "./src/XinYeNianTi-2.otf"
    save_path = "./result/"
    word2pic(txt_path, ttf_path, save_path, 30, './src/bg.png', 40, 20)
