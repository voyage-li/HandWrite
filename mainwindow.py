# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageFont, ImageDraw, ImageQt

import word2pic


class Ui_MainWindow(QtWidgets.QWidget):
    data_path = ''
    ttf_path = ''
    bg_path = ''
    font_x = 0
    font_y = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(435, 293)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(435, 293))
        MainWindow.setMaximumSize(QtCore.QSize(435, 293))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(435, 267))
        self.centralwidget.setMaximumSize(QtCore.QSize(435, 267))
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 110, 401, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.toolButton = QtWidgets.QToolButton(self.widget_2)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 401, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 417, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 170, 401, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(20, 200, 401, 21))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_4.addWidget(self.spinBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.spinBox.setValue(35)
        self.spinBox_2.setValue(50)
        self.spinBox_3.setValue(50)

        # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        self.toolButton.clicked.connect(self.get_txt_path)
        self.toolButton_2.clicked.connect(self.get_ttf_path)
        self.comboBox_2.currentIndexChanged.connect(self.ttf_change)
        self.toolButton_3.clicked.connect(self.get_bg_path)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        save = QFileDialog.getSaveFileName(self, 'save', './', 'pdf(*.pdf)')
        save_path = re.sub(r'([^/]+).pdf', "", save[0]+'.pdf')
        self.font_x = self.spinBox.value()
        margin_x = self.spinBox_2.value()
        margin_y = self.spinBox_3.value()
        if len(save) == 0 or len(self.data_path) == 0 or self.font_x == 0 or len(self.bg_path) == 0 or margin_x == 0 or margin_y == 0:
            return

        result = word2pic.word2pic(self.data_path, self.ttf_path, save_path, self.font_x, self.bg_path, margin_x, margin_y)

        pngFiles = []
        sources = []
        if result != 0:
            for i in range(1, result):
                pngFiles.append(save_path + str(i) + ".png")

        pngFiles.sort()
        output = Image.open(pngFiles[0])
        pngFiles.pop(0)
        output = output.convert("RGB")
        for file in pngFiles:
            pngFile = Image.open(file)
            if pngFile.mode == "RGBA":
                pngFile = pngFile.convert("RGB")
            sources.append(pngFile)
        output.save(save[0]+'.pdf', "pdf", save_all=True, append_images=sources)
        if sys.platform == 'linux':
            os.system('google-chrome '+save[0]+'.pdf')
        else:
            os.startfile(save[0]+'.pdf')

    def get_txt_path(self):
        path_name, _ = QFileDialog.getOpenFileName(self, 'Open file', './', 'data files (*.txt *.md)')
        if len(path_name) == 0:
            return
        self.data_path = path_name
        count = self.comboBox.count()
        now = -1
        for iter in range(count):
            if self.comboBox.itemText(iter) == path_name:
                now = iter
        if now == -1:
            self.comboBox.addItem(path_name)
            count = count + 1
        else:
            count = now + 1
        self.comboBox.setCurrentIndex(count-1)

    def draw_head_pic(self, ttf):
        img = Image.new('RGB', (417, 70), (255, 255, 255))
        font_size = 50
        font = ImageFont.truetype(ttf, font_size)  # 设置字体
        string = '手写模拟'
        draw = ImageDraw.Draw(img)
        draw.text((128-5, 7), string[0], (0, 0, 0), font=font)
        draw.text((168-5, 7), string[1], (0, 0, 0), font=font)
        draw.text((208-5, 7), string[2], (0, 0, 0), font=font)
        draw.text((248-5, 7), string[3], (0, 0, 0), font=font)
        return img

    def ttf_change(self):
        path_name = self.comboBox_2.currentText()
        img = self.draw_head_pic(path_name)
        pix = ImageQt.toqpixmap(img)
        self.label_3.setPixmap(pix)
        # self.label_3.setStyleSheet("border: 2px solid red")
        self.label_3.setScaledContents(True)  # 自适应QLabel大小

    def get_ttf_path(self):
        path_name, _ = QFileDialog.getOpenFileName(self, 'Open file', './', 'font-family files (*.ttf *.otf *.ttc)')
        if len(path_name) == 0:
            return
        self.ttf_path = path_name
        count = self.comboBox_2.count()
        now = -1
        for iter in range(count):
            if self.comboBox_2.itemText(iter) == path_name:
                now = iter
        if now == -1:
            self.comboBox_2.addItem(path_name)
            count = count + 1
        else:
            count = now + 1
        self.comboBox_2.setCurrentIndex(count-1)
        # path_name = self.comboBox_2.currentText()
        # img = self.draw_head_pic(path_name)
        # pix = ImageQt.toqpixmap(img)
        # self.label_3.setPixmap(pix)
        # # self.label_3.setStyleSheet("border: 2px solid red")
        # self.label_3.setScaledContents(True)  # 自适应QLabel大小

    def get_bg_path(self):
        path_name, _ = QFileDialog.getOpenFileName(self, 'Open file', './', 'Image files (*.jpg *.gif *.png *.jpeg)')
        if len(path_name) == 0:
            return
        self.bg_path = path_name
        count = self.comboBox_3.count()
        now = -1
        for iter in range(count):
            if self.comboBox_3.itemText(iter) == path_name:
                now = iter
        if now == -1:
            self.comboBox_3.addItem(path_name)
            count = count + 1
        else:
            count = now + 1
        self.comboBox_3.setCurrentIndex(count-1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HandWrite"))
        self.label.setText(_translate("MainWindow", "文件路径："))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "字体路径："))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "手写模拟"))
        self.pushButton.setText(_translate("MainWindow", "生成"))
        self.label_4.setText(_translate("MainWindow", "背景路径："))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "横向字数："))
        self.label_6.setText(_translate("MainWindow", "横向页边:"))
        self.label_7.setText(_translate("MainWindow", "纵向页边:"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
