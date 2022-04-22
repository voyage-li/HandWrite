import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def word2pic(txt, ttf, save, font_x, bg_image, dis_x, dis_y):
    # 源文件 字体 保存路径 一行显示字体个数 背景图片 页边距横向 页边距纵向
    img = Image.open(bg_image)
    img_wid, img_height = img.size

    font_size = (img_wid-dis_x*2)//(font_x)
    font_y = (img_height-dis_y*2)//(font_size)  # 竖行字体个数计算

    font = ImageFont.truetype(ttf, font_size)  # 设置字体

    f = open(txt, 'r', encoding='utf-8')
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        draw = ImageDraw.Draw(img)
        for i in range(font_y):
            for j in range(font_x):
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((dis_x+(font_size)*j+random.uniform(-2.4, 2.4), dis_y+(font_size+1)*i+random.uniform(-2.4, 2.4)), string[flag], (0, 0, 0), font=font)
                flag += 1
            if flag >= lenstr:
                break
        img.save(save + str(page) + ".png")
        page += 1


if __name__ == "__main__":
    txt_path = './test.txt'
    ttf_path = "./src/test.TTF"
    save_path = "./"
    word2pic(txt_path, ttf_path, save_path, 40, './src/bg.png', 40, 40)
