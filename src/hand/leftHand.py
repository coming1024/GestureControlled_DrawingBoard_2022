import operator
import os

from PyQt5.QtWidgets import QMessageBox

from src.common.base import IMG_CANVAS
from src.common.constant import *
from src.hand.finger import fingerMap
from src.hand.hand import Hand, HandTag
from src.image.draw import *

HEIGHT = 78
LEFT_DIS = 150

left_select = [0, 1, 1, 0, 0]  # 选择状态23指并拢
first = [0, 1, 0, 0, 0]
second = [0, 1, 1, 0, 0]
third = [0, 1, 1, 1, 0]
fourth = [0, 1, 1, 1, 1]
closeOperation = [1, 1, 1, 1, 1]  # 关闭展开栏

shapeType = None
shapeArray = [1, 1, 0, 0, 0]
x1, y1, x2, y2 = -1, -1, -1, -1
IMG_INDEX = 0


# IMG = IMG_CANVAS


def saveFile(mainwindow=None):
    mainwindow.chooseLabel("保存文件")
    global IMG_INDEX
    while os.path.exists(f"result{IMG_INDEX}.jpg"):
        IMG_INDEX = IMG_INDEX + 1

    cv2.imwrite(f"result{IMG_INDEX}.jpg", IMG_CANVAS)
    mainwindow.btnColorBack()
    Hand.FirstFlag = 0
    msg_box = QMessageBox(QMessageBox.Warning, '提示', '文件保存成功！')
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.button(QMessageBox.Ok).animateClick(1000)
    msg_box.exec_()



def openFile(mainwindow=None):
    mainwindow.chooseLabel("打开文件")
    img_canvas = cv2.imread(OpenPath)
    cv2.resize(img_canvas, (IMG_WIDTH, IMG_HEIGHT))
    for i in range(IMG_HEIGHT):
        for j in range(IMG_WIDTH):
            IMG_CANVAS[i, j] = img_canvas[i, j]

    mainwindow.btnColorBack()
    Hand.FirstFlag = 0


def newFile(mainwindow=None):
    mainwindow.chooseLabel("新建文件")
    print("enterNewFile")
    # saveFile()
    # IMG_CANVAS = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
    global IMG_INDEX
    while os.path.exists(f"result{IMG_INDEX}.jpg"):
        IMG_INDEX = IMG_INDEX + 1
    cv2.imwrite(f"result{IMG_INDEX}.jpg", IMG_CANVAS)  # 保存
    msg_box = QMessageBox(QMessageBox.Warning, '提示', '文件保存成功！')
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.button(QMessageBox.Ok).animateClick(1000)
    msg_box.exec_()

    print("saveAlready")

    for i in range(IMG_HEIGHT):
        for j in range(IMG_WIDTH):
            IMG_CANVAS[i, j] = 0

    mainwindow.btnColorBack()
    Hand.FirstFlag = 0


class LeftHand(Hand):
    def __init__(self):
        super().__init__()
        self.tag = HandTag.LEFT

    def judgeCurve(self, finger):
        var = fingerMap.get(finger)
        if finger == 0:
            return True if self.lms[var][1] < self.lms[var - 1][1] else False
        return True if self.lms[var][2] > self.lms[var - 2][2] else False

    def judgeSelect(self):  # 判断是否为左手选择状态
        id1, x1, y1 = self.getSecond()
        id2, x2, y2 = self.getThird()
        return abs(x1 - x2) <= 80

    def checkSelect(self, img):
        fingers = self.getFingers()
        if fingers is not None and len(fingers) != 0:
            if operator.eq(fingers, left_select) and self.judgeSelect():
                id2, x2, y2 = self.getSecond()
                id3, x3, y3 = self.getThird()
                # 这里画一个矩形
                cv2.rectangle(img, (x3 - 10, y3 - 10), (x2 + 10, y2 + 10), PEN.penColor, cv2.FILLED)
                return True
        else:
            return False

    def penWidth(self, mainWindow):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, first):
            PEN.penThickness = PenThickness1
            Hand.SecondFlag = 1
            mainWindow.chooseLabel("宽度细")
        elif operator.eq(fingers, second):
            PEN.penThickness = PenThickness2
            Hand.SecondFlag = 2
            mainWindow.chooseLabel("宽度中等")
        elif operator.eq(fingers, third):
            PEN.penThickness = PenThickness3
            Hand.SecondFlag = 3
            mainWindow.chooseLabel("宽度粗")
        elif operator.eq(fingers, closeOperation):
            mainWindow.penBoardHide()
            Hand.FirstFlag = 0
            Hand.SecondFlag = 0

    def erase(self, mainWindow):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        PEN.penColor = BLACK
        if operator.eq(fingers, first):
            PEN.penThickness = EraserThickness1
            Hand.SecondFlag = 1
            mainWindow.chooseLabel("宽度细")
        elif operator.eq(fingers, second):
            PEN.penThickness = EraserThickness2
            Hand.SecondFlag = 2
            mainWindow.chooseLabel("宽度中等")
        elif operator.eq(fingers, third):
            PEN.penThickness = EraserThickness3
            Hand.SecondFlag = 3
            mainWindow.chooseLabel("宽度粗")
        elif operator.eq(fingers, closeOperation):
            mainWindow.closeEraser()
            Hand.FirstFlag = 0
            Hand.SecondFlag = 0

    def shape(self, mainWindow, img, hand):
        global shapeArray
        fingers = self.getFingers()
        if self.judgeNull():
            return
        rightHandFingers = hand.getFingers()
        global x1, y1, x2, y2

        # 正方形
        if operator.eq(fingers, first):
            Hand.SecondFlag = 1
            mainWindow.chooseLabel("形状矩形")
        # 圆形
        elif operator.eq(fingers, second):
            Hand.SecondFlag = 2
            mainWindow.chooseLabel("形状圆形")
        # 三角形
        elif operator.eq(fingers, third):
            Hand.SecondFlag = 3
            mainWindow.chooseLabel("形状三角形")
        elif operator.eq(fingers, fourth):
            pass

        if operator.eq(rightHandFingers, shapeArray):
            id1, x1, y1 = hand.getFirst()
            id2, x2, y2 = hand.getSecond()
            # 正方形
            if Hand.SecondFlag == 1:
                drawRectangle(img, x1, y1, x2, y2)
            # 圆形
            elif Hand.SecondFlag == 2:
                drawCircle(img, x1, y1, x2, y2)
            # 三角形
            elif Hand.SecondFlag == 3:
                drawTriangle(img, x1, y1, x2, y2)
            elif operator.eq(fingers, fourth):
                pass
        elif operator.eq(rightHandFingers, closeOperation):
            if x1 != -1 and y1 != -1 and x2 != -1 and y2 != -1:
                if Hand.SecondFlag == 1:
                    drawRectangle(IMG_CANVAS, x1, y1, x2, y2)
                elif Hand.SecondFlag == 2:
                    drawCircle(IMG_CANVAS, x1, y1, x2, y2)
                elif Hand.SecondFlag == 3:
                    drawTriangle(IMG_CANVAS, x1, y1, x2, y2)
                Hand.SecondFlag = 0
        if operator.eq(fingers, closeOperation):
            mainWindow.shapeBoardHide()
            Hand.SecondFlag = 0
            Hand.FirstFlag = 0

    def penColor(self, mainWindow):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, first):
            PEN.penColor = WHITE
            Hand.SecondFlag = 1
            mainWindow.chooseLabel("颜色白色")
        elif operator.eq(fingers, second):
            PEN.penColor = BLUE
            Hand.SecondFlag = 2
            mainWindow.chooseLabel("颜色蓝色")
        elif operator.eq(fingers, third):
            PEN.penColor = GREEN
            Hand.SecondFlag = 3
            mainWindow.chooseLabel("颜色绿色")
        elif operator.eq(fingers, fourth):
            PEN.penColor = YELLOW
            Hand.SecondFlag = 4
            mainWindow.chooseLabel("颜色黄色")
        elif operator.eq(fingers, closeOperation):
            mainWindow.colorBoardHide()
            Hand.SecondFlag = 0
            Hand.FirstFlag = 0

    def process(self, img, hand, mainWindow=None):
        global LEFT_DIS, HEIGHT
        if not self.judgeNull():
            if self.checkSelect(img) and Hand.FirstFlag == 0:
                print("select")
                id2, x2, y2 = self.getSecond()
                if x2 < LEFT_DIS:
                    if y2 < HEIGHT:  # 画笔粗细
                        mainWindow.penBoardShow()
                        Hand.FirstFlag = 1
                    elif HEIGHT < y2 < 2 * HEIGHT:  # 橡皮擦
                        mainWindow.eraserBtn()
                        Hand.FirstFlag = 2
                    elif 2 * HEIGHT < y2 < 3 * HEIGHT:  # 形状
                        mainWindow.shapeBoardShow()
                        Hand.FirstFlag = 3
                    elif 3 * HEIGHT < y2 < 4 * HEIGHT:  # 画笔颜色
                        mainWindow.colorBoardShow()
                        Hand.FirstFlag = 4
                    elif 4 * HEIGHT < y2 < 5 * HEIGHT:  # 新建
                        mainWindow.newBtn()
                        Hand.FirstFlag = 5
                    elif 5 * HEIGHT < y2 < 6 * HEIGHT:  # 打开
                        mainWindow.newOpen()
                        Hand.FirstFlag = 6
                    elif 6 * HEIGHT < y2 < 7 * HEIGHT:  # 保存
                        mainWindow.saveBtn()
                        Hand.FirstFlag = 7

            elif not self.checkSelect(img):
                if Hand.FirstFlag == 1:
                    self.penWidth(mainWindow)
                elif Hand.FirstFlag == 2:
                    self.erase(mainWindow)
                elif Hand.FirstFlag == 3:
                    self.shape(mainWindow, img, hand)
                elif Hand.FirstFlag == 4:
                    self.penColor(mainWindow)
                elif Hand.FirstFlag == 5:
                    newFile(mainWindow)
                elif Hand.FirstFlag == 6:
                    openFile(mainWindow)
                elif Hand.FirstFlag == 7:
                    saveFile(mainWindow)
