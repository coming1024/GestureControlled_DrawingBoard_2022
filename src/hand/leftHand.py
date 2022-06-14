import operator

import cv2
# from src.main import PaintWindow

from src.common.base import PEN
from src.common.constant import GREEN, PURPLE, RED, PenRadius
from src.hand.finger import fingerMap
from src.hand.hand import Hand, HandTag


Pen_flag = False

left_select = [0, 1, 0, 0, 0]
greenColor = [0, 1, 1, 0, 0]
purpleColor = [0, 1, 1, 1, 0]
blueColor = [0, 1, 1, 1, 1]

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
            if operator.eq(fingers, left_select):
                return True
        else:
            return False

    def selectPen(self):
        fingers=self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, greenColor):
            print("green")
            PEN.penColor = GREEN
        elif operator.eq(fingers, purpleColor):
            print("purple")
            PEN.penColor = PURPLE
        elif operator.eq(fingers, blueColor):
            print("blue")
            PEN.penColor = RED

    def process(self,img,anotherHand,mainWindow=None):
        from src.main import PaintWindow
        global Pen_flag
        if not self.judgeNull():
            if self.checkSelect() and not Pen_flag:
                print("select")
                # mainWindow.clickButton("select")
                lid_2, lx2, ly2 = self.getSecond()
                cv2.circle(img, (lx2, ly2), PenRadius, PEN.penColor, cv2.FILLED)
                if lx2 < 200 and ly2 < 200:
                    # mainWindow.clickButton("selectPen")
                    # PaintWindow.penBoardShow()
                    Pen_flag = True
                    print("select_Pen_flag = 1")
            if not self.checkSelect() and Pen_flag:
                print("enter")
                self.selectPen()
                Pen_flag = False
            if PEN.penColor == GREEN:
                print("green")
            elif PEN.penColor == PURPLE:
                print("purple")
                pass
            elif PEN.penColor == RED:
                print("red")


