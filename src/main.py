import sys

import cv2
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.common.base import IMG_CANVAS
from src.common.constant import IMG_HEIGHT, IMG_WIDTH
from src.hand import detector
from src.image.detector import reverseImage, detectorImage
from src.image.draw import *
<<<<<<< HEAD
<<<<<<< Updated upstream
from src.ui.BtnFunction.BtnFunction import *
from src.ui.InterfaceUI_01 import *
=======
# from src.ui.window import *
from src.ui.InterfaceUI_01 import *

draw = [0, 1, 0, 0, 0]
rectangle = [1, 1, 0, 0, 0]
stopRectangle = [1, 1, 0, 0, 1]
triangle = [1, 1, 1, 0, 0]
stop = [0, 1, 1, 0, 0]

# greenColor = [0, 1, 0, 0, 0]
# purpleColor = [0, 1, 1, 0, 0]
# blueColor = [0, 1, 1, 1, 0]

left_select = [0, 1, 0, 0, 0]
greenColor = [0, 1, 1, 0, 0]
purpleColor = [0, 1, 1, 1, 0]
blueColor = [0, 1, 1, 1, 1]

Pen_flag = False
# selectPen_flag = 0

def usePen(img, leftHand):
    leftFingers = leftHand.getFingers()

    if leftFingers is not None and len(leftFingers) != 0:
        # if operator.eq(leftFingers, left_select):
        #     # print(self.prex,self.prey)
        #     print("select")
        #     PEN.penColor = YELLOW
        if operator.eq(leftFingers, greenColor):
            print("green")
            PEN.penColor = GREEN
        elif operator.eq(leftFingers, purpleColor):
            print("purple")
            PEN.penColor = PURPLE
        elif operator.eq(leftFingers, blueColor):
            print("blue")
            PEN.penColor = RED


def useErase(img):
    pass
>>>>>>> Stashed changes

global Templ_Change
Templ_Change = 0

<<<<<<< Updated upstream
=======
from src.ui.InterfaceUI_01 import *

>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3
CAP = cv2.VideoCapture(0)
CAP.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
CAP.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
HAND_DETECTOR = detector.HandDetector(detectionCon=0.8, trackCon=0.8)
<<<<<<< HEAD
=======
def checkSelect(img, leftHand):
    leftFingers = leftHand.getFingers()
    if leftFingers is not None and len(leftFingers) != 0:
        if operator.eq(leftFingers, left_select):
            return True
    else:
        return False

>>>>>>> Stashed changes
=======
>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3

def imgInit():
    success, img = CAP.read()
    img = reverseImage(img)
    img = HAND_DETECTOR.drawHands(img)
    HAND_DETECTOR.initPosition(img)
    return success, img

<<<<<<< HEAD
<<<<<<< Updated upstream

class PaintWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    select_Pen_flag = False

=======
class MainWindow(QMainWindow, Ui_MainWindow):
    select_Pen_flag = False
>>>>>>> Stashed changes
=======

class MainWindow(QMainWindow, Ui_MainWindow):
    select_Pen_flag = False

>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3
    def __init__(self, parent=None):
        # super(MainWindow, self).__init__(parent)
        # self.setupUi(self)
        # self.timer_camera = QTimer(self)
        # self.timer_camera.timeout.connect(self.draw)
        # self.timer_camera.start(5)
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute((QtCore.Qt.WA_TranslucentBackground))
        self.penBoardHide()
        self.pushButton_4.clicked.connect(self.penBoardShow)  # 点击画笔按钮
        self.pushButton_15.clicked.connect(self.penBoardHide)  # 隐藏画笔菜单
        self.shapeBoardHide()
        self.pushButton_6.clicked.connect(self.shapeBoardShow)  # 点击形状按钮
        self.pushButton_14.clicked.connect(self.shapeBoardHide)  # 隐藏形状菜单
        self.colorBoardHide()
        self.pushButton_16.clicked.connect(self.colorBoardShow)  # 点击颜色按钮
        self.pushButton_13.clicked.connect(self.colorBoardHide)  # 隐藏形状菜单
        self.pushButton_5.clicked.connect(self.eraserBtn)  # 点击橡皮按钮
        self.pushButton_9.clicked.connect(self.saveBtn)  # 点击保存按钮
        self.pushButton_7.clicked.connect(self.newBtn)  # 点击新建按钮
        BtnFunction.PreParement(self)
        BtnFunction.UiShaw(self)
        self.show()
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.draw)
        self.timer_camera.start(5)

    def draw(self):
        success, img = imgInit()

<<<<<<< HEAD
<<<<<<< Updated upstream
        leftHand = HAND_DETECTOR.leftHand
        rightHand = HAND_DETECTOR.rightHand
        leftHand.process(img, rightHand, self)
        rightHand.process(img, leftHand)
=======
        rightHand = HAND_DETECTOR.rightHand
        rightFingers = rightHand.getFingers()

        leftHand = HAND_DETECTOR.leftHand
        leftFingers = leftHand.getFingers()

        if leftFingers is not None and len(leftFingers) != 0:
            leftHand.exist = True
            if checkSelect(img, leftHand) and not Pen_flag:
                print("select")
                self.clickButton("select")
                lid_2, lx2, ly2 = leftHand.getSecond()
                cv2.circle(img, (lx2, ly2), PenRadius, PEN.penColor, cv2.FILLED)
                if lx2 < 200 and ly2 < 200:
                    self.clickButton("selectPen")
                    Pen_flag = True
                    print("select_Pen_flag = 1")
            if not checkSelect(img, leftHand) and Pen_flag:
                print("enter")
                usePen(img, leftHand)
                Pen_flag = False
            if PEN.penColor == GREEN:
                self.clickButton("green")
                # self.clickButton(self, "green")
            elif PEN.penColor == PURPLE:
                print("purple")
                self.clickButton("purple")
            elif PEN.penColor == RED:
                print("red")
                self.clickButton("red")

        else:
            leftHand.exist = False

        # 如果手指出现在屏幕中
        if rightFingers is not None and len(rightFingers) != 0:
            # self.clickButton()
            rightHand.exist = True
            id1, x1, y1 = rightHand.getFirst()
            id2, x2, y2 = rightHand.getSecond()
            id3, x3, y3 = rightHand.getThird()
            id4, x4, y4 = rightHand.getFourth()
            id5, x5, y5 = rightHand.getFifth()
            # 对于以下情况不同的策略,可能需要定义若干接口
            if operator.eq(rightFingers, draw):
                # 如果食指伸出来了并且中指没有伸出来，就要画圈
                cv2.circle(img, (x2, y2), PenRadius, PEN.penColor, cv2.FILLED)
                if self.prex != -1 or self.prey != -1:
                    # print("draw line")
                    cv2.line(IMG_CANVAS, (x2, y2), (self.prex, self.prey), PEN.penColor, PEN.penThickness,
                             cv2.FILLED)
            elif operator.eq(rightFingers, rectangle):
                drawRectangle(img, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(rightFingers, stopRectangle):
                drawRectangle(IMG_CANVAS, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(rightFingers, triangle):
                drawTriangle(img, (x1, y1), (x2, y2), (x3, y3), PEN.penColor)
            elif operator.eq(rightFingers, [0, 1, 0, 0, 1]):
                if PEN.penColor == PURPLE:
                    PEN.penColor = GREEN
                else:
                    PEN.penColor = PURPLE
            elif operator.eq(rightFingers, stop):
                pass
            self.prex, self.prey = x2, y2
        else:
            rightHand.exist = False
            self.prex, self.prey = -1, -1
>>>>>>> Stashed changes

        img = detectorImage(img, IMG_CANVAS)
        showImage = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888)
        # showImage = QImage(IMG_CANVAS.data, IMG_CANVAS.shape[1], IMG_CANVAS.shape[0], QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(showImage))  # 将摄像头显示在之前创建的Label控件中
=======
        leftHand=HAND_DETECTOR.leftHand
        rightHand=HAND_DETECTOR.rightHand
        leftHand.process(img,rightHand,self)
        rightHand.process(img,leftHand)

        img = detectorImage(img, IMG_CANVAS)
        showImage=QImage(img.data,img.shape[1],img.shape[0],QImage.Format_BGR888)
        # showImage = QImage(IMG_CANVAS.data, IMG_CANVAS.shape[1], IMG_CANVAS.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))  # 将摄像头显示在之前创建的Label控件中
>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3
        # self.timer_camera.start(1)
        # cv2.imshow("Img", img)
        cv2.imshow("canvas", IMG_CANVAS)

<<<<<<< HEAD
    # 浮窗
    def PageChange(self):
        global Templ_Change
        if Templ_Change == 0:
            self.showMaximized()
            Templ_Change = 1
            return
        if Templ_Change == 1:
            self.showNormal()
            Templ_Change = 0

    def mousePressEvent(self, e):
        if e.pos().x() < 150:
            BtnFunction.MeauExpend(self)

    # 画笔隐藏
    def penBoardHide(self):
        self.frame_5.setVisible(False)

    # 画笔展示
    def penBoardShow(self):
        self.frame_6.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_5.setVisible(True)
        self.btnColorBack()
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 形状隐藏
    def shapeBoardHide(self):
        self.frame_6.setVisible(False)

    # 形状展示
    def shapeBoardShow(self):
        self.frame_5.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_6.setVisible(True)
        self.btnColorBack()
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 颜色隐藏
    def colorBoardHide(self):
        self.frame_8.setVisible(False)

    # 颜色展示
    def colorBoardShow(self):
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_8.setVisible(True)
        self.btnColorBack()
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 点击橡皮
    def eraserBtn(self):
        self.frame_6.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_5.setVisible(True)
        self.btnColorBack()
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 点击保存
    def saveBtn(self):
        self.btnColorBack()
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 点击新建
    def newBtn(self):
        self.btnColorBack()
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:7px solid #ffd194;\n"
"    border-radius:9px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"}\n")

    # 恢复按钮颜色
    def btnColorBack(self):
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    font: 17pt \"仿宋\";\n"
"    color:rgba(200, 200,200, 255);\n"
"    border-left:3px solid rgba(200, 200, 200, 255);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
"    }\n"
"QPushButton:pressed{\n"
"    border-left:7px solid #ffd194;\n"
"    background-color:rgba(0,0,0,40);\n"
"    border-bottom-right-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    }")
=======
>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    UI = PaintWindow()
    UI.show()
    sys.exit(app.exec_())