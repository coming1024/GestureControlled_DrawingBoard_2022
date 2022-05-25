import operator
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.common.base import *
from src.image.detector import *
from src.image.draw import *
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


def checkSelect(img, leftHand):
    leftFingers = leftHand.getFingers()
    if leftFingers is not None and len(leftFingers) != 0:
        if operator.eq(leftFingers, left_select):
            return True
    else:
        return False


def imgInit():
    success, img = CAP.read()
    img = reverseImage(img)
    img = HAND_DETECTOR.drawHands(img)
    HAND_DETECTOR.initPosition(img)
    return success, img

class MainWindow(QMainWindow, Ui_MainWindow):
    select_Pen_flag = False
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.draw)
        self.timer_camera.start(5)

        self.prex, self.prey = -1, -1

    def draw(self):

        global Pen_flag
        success, img = imgInit()

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

        img = detectorImage(img, IMG_CANVAS)

        showImage = QImage(IMG_CANVAS.data, IMG_CANVAS.shape[1], IMG_CANVAS.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))  # 将摄像头显示在之前创建的Label控件中
        # self.timer_camera.start(1)
        cv2.imshow("Img", img)
        # cv2.imshow("canvas", imgCanvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
