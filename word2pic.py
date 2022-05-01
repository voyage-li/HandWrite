import imp
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import random
import re


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
        i = 0
        while i+1.5*font_size < img_height-dis_y:
            j = 0
            while j + 1.5*font_size < img_wid-dis_x:
                if(iter >= length):
                    break
                if string[iter] == '\n':
                    iter += 1
                    break
                if re.match('[\u4e00-\u9fa5]', f'%c' % string[iter]):
                    draw.text((dis_x+j+random.uniform(-3, 3), dis_y + i + random.uniform(-3, 3)), string[iter], (0, 0, 0), font=font)
                    j += font_size-7
                else:
                    draw.text((dis_x+j, dis_y + i), string[iter], (0, 0, 0), font=font)
                    if re.match('[a-zA-Z0-9]', f'%c' % string[iter]):
                        j += (font_size-7)/2.5
                    else:
                        j += (font_size-7)//2
                iter += 1
            i += font_size+1
        img.save(save + str(page) + ".png", dpi=(150.0, 150.0))
        page += 1
    return page


if __name__ == "__main__":
    txt_path = './src/test.md'
    ttf_path = "./src/AiDeMuGuangWuSuoBuZai-2.ttf"
    save_path = "./result/"
    word2pic(txt_path, ttf_path, save_path, 30, './src/bg.png', 40, 40)
