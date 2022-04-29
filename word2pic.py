from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import random
import sys


def translate(txt):
    f = open(txt, 'r', encoding='utf-8')
    string = f.read()
    f.close()

    return string


def word2pic(txt, ttf, save, font_x, bg_image, dis_x, dis_y):
    # 源文件 字体 保存路径 一行显示字体个数 背景图片 页边距横向 页边距纵向
    img = Image.open(bg_image)
    img_wid, img_height = img.size

    font_size = (img_wid-dis_x*2)//(font_x)
    font_y = (img_height-dis_y*2)//(font_size)  # 竖行字体个数计算

    font = ImageFont.truetype(ttf, font_size)  # 设置字体

    string = translate(txt)

    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open(bg_image)
        draw = ImageDraw.Draw(img)
        for i in range(font_y):
            for j in range(font_x):
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((dis_x+(font_size)*j+random.uniform(-1.5, 1.5), dis_y+(font_size+1)*i+random.uniform(-1.5, 1.5)), string[flag], (0, 0, 0), font=font)
                flag += 1
            if flag >= lenstr:
                break
        img.save(save + str(page) + ".png")
        page += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # txt_path = './test.txt'
    # ttf_path = "./src/test.TTF"
    # save_path = "./"
    # word2pic(txt_path, ttf_path, save_path, 40, './src/bg.png', 40, 40)
