import operator

import cv2

from src.common.base import PEN, IMG_CANVAS
from src.common.constant import PenRadius
from src.hand.finger import fingerMap
from src.hand.hand import Hand, HandTag
from src.image.draw import drawRectangle, drawTriangle

drawMode = [0, 1, 0, 0, 0]
rectangle = [1, 1, 0, 0, 0]
stopRectangle = [1, 1, 0, 0, 1]
triangle = [1, 1, 1, 0, 0]
stop = [0, 1, 1, 0, 0]
prex,prey=0,0

class RightHand(Hand):
    def __init__(self):
        super().__init__()
        self.tag = HandTag.RIGHT

    def judgeCurve(self, finger):
        var = fingerMap.get(finger)
        if finger == 0:
            return True if self.lms[var][1] > self.lms[var - 1][1] else False
        return True if self.lms[var][2] > self.lms[var - 2][2] else False

    def process(self,img,mainWindow=None):
        global prex,prey
        # 如果手指出现在屏幕中
        if self.judgeNull():
            prex, prey = -1, -1
        else:
            fingers=self.getFingers()
            id1, x1, y1 = self.getFirst()
            id2, x2, y2 = self.getSecond()
            id3, x3, y3 = self.getThird()
            id4, x4, y4 = self.getFourth()
            id5, x5, y5 = self.getFifth()

            if operator.eq(fingers, drawMode):
                # 如果食指伸出来了并且中指没有伸出来，就要画圈
                cv2.circle(img, (x2, y2), PenRadius, PEN.penColor, cv2.FILLED)
                if prex != -1 or prey != -1:
                    cv2.line(IMG_CANVAS, (x2, y2), (prex, prey), PEN.penColor, PEN.penThickness,cv2.FILLED)
            elif operator.eq(fingers, rectangle):
                drawRectangle(img, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(fingers, stopRectangle):
                drawRectangle(IMG_CANVAS, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(fingers, triangle):
                drawTriangle(img, (x1, y1), (x2, y2), (x3, y3), PEN.penColor)
            elif operator.eq(fingers, stop):
                pass
            prex, prey = x2, y2


