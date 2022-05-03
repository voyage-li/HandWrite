from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import random
import re

text_re = [
    r'\~\~([^\~]+)\~\~',
    r'\*\*([^\*]+)\*\*',
    r'\_\_([^\_]+)\_\_',
    r'\=\=([^\=]+)\=\=',
    r'\*([^\*]+)\*',
    r'\_([^\_]+)\_',
    r'\`([^\`]+)\`'
]


def list_sub_2(x):
    ans = '\n    '
    ans += '('+x.group(1)+')'+' '+x.group(2)
    return ans


def list_sub_3(x):
    ans = '\n        '
    iter = eval(x.group(1))
    if iter == 1:
        ans += '①'
    elif iter == 2:
        ans += '②'
    elif iter == 3:
        ans += '③'
    elif iter == 4:
        ans += '④'
    elif iter == 5:
        ans += '⑤'
    elif iter == 6:
        ans += '⑥'
    elif iter == 7:
        ans += '⑦'
    elif iter == 8:
        ans += '⑧'
    elif iter == 9:
        ans += '⑨'
    ans += '  '+x.group(2)
    return ans


def list_sub_4(x):
    ans = '\n            #'
    iter = eval(x.group(1))
    ans = ans.replace('#', chr(iter-1+ord('a')))
    ans += ') '+x.group(2)
    return ans


def tittle(x):
    ans = ''
    length = len(x.group(1))
    if length == 1:
        ans += '㍙'
    elif length == 2:
        ans += '㍚'
    elif length == 3:
        ans += '㍛'
    elif length == 4:
        ans += '㍜'
    elif length == 5:
        ans += '㍝'
    elif length == 6:
        ans += '㍞'
    ans += x.group(2)
    return ans


def translate(txt):
    # 画饼 这里要支持简单 markdown
    # to be done
    f = open(txt, 'r', encoding='utf-8')
    string = f.read()
    f.close()
    if '.txt' in txt:
        return string
    # 直接去掉所有有标题的内容
    string = re.sub(r'(#{1,6}) (.+)', tittle, string)
    # 有序无序在一起会很丑陋
    string = re.sub(r'[.\n][\-\+\*] (.+)', lambda x: '\n'+' ● ' + x.group(1), string)
    string = re.sub(r'[.\n][\ ]{4}[\-\+\*] (.+)', lambda x: '\n    '+' ○ ' + x.group(1), string)
    string = re.sub(r'[.\n][\ ]{8}[\-\+\*] (.+)', lambda x: '\n        '+' ■ ' + x.group(1), string)
    string = re.sub(r'[.\n](\d.) (.+)', lambda x: '\n '+x.group(1)+x.group(2), string)
    string = re.sub(r'[.\n][\ ]{4}(\d). (.+)', list_sub_2, string)
    string = re.sub(r'[.\n][\ ]{8}(\d). (.+)', list_sub_3, string)
    string = re.sub(r'[.\n][\ ]{12}(\d). (.+)', list_sub_4, string)
    # 去掉链接
    string = re.sub(r'\[(.+)\]\((.+)\)', lambda x: x.group(1)+'('+x.group(2)+')', string)
    # 去掉text内容
    for iter in text_re:
        string = re.sub(iter, lambda x: x.group(1), string)

    return string


def word2pic(txt, ttf, save, font_x, bg_image, dis_x, dis_y, mess, font_ud):
    # 源文件 字体 保存路径 一行显示字体个数 背景图片 页边距横向 页边距纵向
    img = Image.open(bg_image)
    img_wid, img_height = img.size

    font_size = (img_wid-dis_x*2)//(font_x)+5
    font_size_now = font_size

    # font_y = (img_height-dis_y*2)//(font_size)  # 竖行字体个数计算

    font_basic = ImageFont.truetype(ttf, font_size)  # 设置字体

    tittle_size = '''㍙㍚㍛㍜㍝㍞'''

    string = translate(txt)
    length = len(string)

    page = 1
    iter = 0
    last_j = 0
    while iter < length:
        img = Image.open(bg_image)
        draw = ImageDraw.Draw(img)
        i = 0
        while (i + 3 * font_size) < (img_height - dis_y):
            if(iter >= length):
                break
            j = 0
            is_tittle = tittle_size.find(string[iter]) + 1
            if is_tittle == 0:
                font_size_now = font_size
                is_tittle = 7
            else:
                font_size_now = font_size + round(font_size/6) * (round(font_size/5) - is_tittle)
                iter += 1
            while (j + 3 * font_size) < (img_wid - dis_x):
                if is_tittle == 7:
                    font = font_basic
                else:
                    font = ImageFont.truetype(ttf, font_size_now)
                if abs(random.randint(-10, 10)) > 7:
                    font = ImageFont.truetype(ttf, font_size_now + random.randint(-font_ud, font_ud))
                if(iter >= length):
                    break
                if string[iter] == '\n':
                    iter += 1
                    break

                if re.match('[\u4e00-\u9fa5]', f'%c' % string[iter]):
                    draw.text((dis_x + j + random.uniform(-mess, mess) - (7 - is_tittle), dis_y + i + random.uniform(-mess, mess)), string[iter], (0, 0, 0), font)
                    j += font_size_now - round(font_size/6)
                else:
                    if i != 0 and j == 0 and re.match('[\.\。\,\，\:\：\!\！\?\？\”\;\；\]\}\)]', f'%c' % string[iter]):
                        draw.text((dis_x + last_j - round(font_size/30)*(7 - is_tittle), dis_y + i - font_size_now - round(font_size/4)), string[iter], (0, 0, 0), font)
                    else:
                        if string[iter] == '○' or string[iter] == '●' or string[iter] == '■':
                            draw.text((dis_x + j - round(font_size/30)*(7 - is_tittle), dis_y + i + font_size_now//2), string[iter], (0, 0, 0), ImageFont.truetype(ttf, font_size//3))
                        else:
                            draw.text((dis_x + j - round(font_size/30)*(7 - is_tittle), dis_y + i), string[iter], (0, 0, 0), font)
                    if re.match('[a-zA-Z]', f'%c' % string[iter]):
                        j += (font_size_now-round(font_size/4))/2.5
                    elif re.match('[0-9]', f'%c' % string[iter]):
                        j += (font_size_now-round(font_size/4))//2
                    else:
                        j += (font_size_now-round(font_size/4))//3
                iter += 1
                last_j = j
            i += font_size_now + round(font_size/4)
        img.save(save + str(page) + ".png", dpi=(150.0, 150.0))
        page += 1
    return page


if __name__ == "__main__":
    txt_path = './src/test.md'
    ttf_path = "./src/AiDeMuGuangWuSuoBuZai-2.ttf"
    save_path = "./"
    word2pic(txt_path, ttf_path, save_path, 40, './src/bg.png', 80, 80, 2, 1)
