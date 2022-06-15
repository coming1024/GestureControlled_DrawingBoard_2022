import operator

import cv2
# import src.main
# import src.ui.MyMethod as Method
# from src.main import PaintWindow
# from src.ui.InterfaceUI_01 import Ui_MainWindow
from src.common.base import PEN
from src.common.constant import GREEN, PURPLE, RED, PenRadius
from src.hand.finger import fingerMap
from src.hand.hand import Hand, HandTag

Pen_flag = 0

left_select = [0, 1, 1, 0, 0]  # 选择状态23指并拢
second = [0, 1, 1, 0, 0]
third = [0, 1, 1, 1, 0]
fourth = [0, 1, 1, 1, 1]
closeOperation = [1, 1, 1, 1, 1]   #关闭展开栏


class LeftHand(Hand):
    def __init__(self):
        super().__init__()
        self.tag = HandTag.LEFT

    def judgeCurve(self, finger):
        var = fingerMap.get(finger)
        if finger == 0:
            return True if self.lms[var][1] < self.lms[var - 1][1] else False
        return True if self.lms[var][2] > self.lms[var - 2][2] else False

    def checkSelect(self):
        fingers = self.getFingers()
        if fingers is not None and len(fingers) != 0:
            if operator.eq(fingers, left_select) and self.judgeSelect():
                return True
        else:
            return False

    def selectPen(self):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, second):
            print("green")
            PEN.penColor = GREEN
        elif operator.eq(fingers, third):
            print("purple")
            PEN.penColor = PURPLE
        elif operator.eq(fingers, fourth):
            print("blue")
            PEN.penColor = RED

    def process(self, img, anotherHand, mainWindow=None):

        global Pen_flag
        if not self.judgeNull():
            if self.checkSelect() and Pen_flag==0:
                print("select")
                # mainWindow.clickButton("select")
                lid_2, lx2, ly2 = self.getSecond()
                cv2.circle(img, (lx2, ly2), PenRadius, PEN.penColor, cv2.FILLED)
                if lx2 < 150 and ly2 < 100:  # 画笔粗细
                    mainWindow.penBoardShow()
                    Pen_flag = 1
                    print("select_Pen_flag = 1")
                elif lx2 < 150 and ly2 > 100 and ly2 < 200:  # 橡皮擦
                    mainWindow.eraserBtn()
                    Pen_flag = 2
                    print("select_Pen_flag = 2")
                elif lx2 < 150 and ly2 > 200 and ly2 < 300:  # 形状
                    mainWindow.shapeBoardShow()
                    Pen_flag = 3
                    print("select_Pen_flag = 3")
                elif lx2 < 150 and ly2 > 300 and ly2 < 400:  # 画笔颜色
                    mainWindow.colorBoardShow()
                    Pen_flag = 4
                    print("select_Pen_flag = 4")

            fingers = self.getFingers()
            if not self.checkSelect() and Pen_flag==1:
                print("select_Pen_width")
                # self.selectPen()
                Pen_flag = 0
                if operator.eq(fingers, closeOperation):
                    mainWindow.penBoardHide()

            elif not self.checkSelect() and Pen_flag == 2:
                print("select_rubber")
                # self.selectPen()
                Pen_flag = 0
                if operator.eq(fingers, closeOperation):
                    mainWindow.closeEraser()

            elif not self.checkSelect() and Pen_flag == 3:
                print("select_shape")
                # self.selectPen()
                Pen_flag = 0
                if operator.eq(fingers, closeOperation):
                    mainWindow.shapeBoardHide()

            elif not self.checkSelect() and Pen_flag == 4:
                print("select_Pen_color")
                self.selectPen()
                Pen_flag = 0
                if operator.eq(fingers, closeOperation):
                    mainWindow.colorBoardHide()