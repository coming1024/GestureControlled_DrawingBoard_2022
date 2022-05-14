import operator
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.common.base import *
from src.image.detector import *
from src.image.draw import *
from src.ui.window import *

draw = [0, 1, 0, 0, 0]
rectangle = [1, 1, 0, 0, 0]
stopRectangle = [1, 1, 0, 0, 1]
triangle = [1, 1, 1, 0, 0]
stop = [0, 1, 1, 0, 0]


def imgInit():
    success, img = CAP.read()
    img = reverseImage(img)
    img = HAND.drawHands(img)
    lmList = HAND.getPosition(img, draw=False)
    figures = HAND.getFigures()
    return success, img, lmList, figures


class MainWindow(QMainWindow, UIMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.draw)
        self.timer_camera.start(5)

        self.prex, self.prey = -1, -1

    def draw(self):
        success, img, lmList, figures = imgInit()
        # 如果手指出现在屏幕中
        if figures is not None and len(figures) != 0:
            id1, x1, y1 = HAND.getFirst()
            id2, x2, y2 = HAND.getSecond()
            id3, x3, y3 = HAND.getThird()
            id4, x4, y4 = HAND.getFourth()
            id5, x5, y5 = HAND.getFifth()
            # 对于以下情况不同的策略,可能需要定义若干接口
            id2, x2, y2 = HAND.getSecond()
            if operator.eq(figures, draw):
                # 如果食指伸出来了并且中指没有伸出来，就要画圈
                cv2.circle(img, (x2, y2), PenRadius, PEN.penColor, cv2.FILLED)
                if self.prex != -1 or self.prey != -1:
                    # print("draw line")
                    cv2.line(IMG_CANVAS, (x2, y2), (self.prex, self.prey), PEN.penColor, PEN.penThickness,
                             cv2.FILLED)
            elif operator.eq(figures, rectangle):
                drawRectangle(img, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(figures, stopRectangle):
                drawRectangle(IMG_CANVAS, (x1, y1), (x2, y2), PEN.penColor)
            elif operator.eq(figures, triangle):
                drawTriangle(img, (x1, y1), (x2, y2), (x3, y3), PEN.penColor)
            elif operator.eq(figures, [0, 1, 0, 0, 1]):
                if PEN.penColor == PURPLE:
                    PEN.penColor = GREEN
                else:
                    PEN.penColor = PURPLE
            elif operator.eq(figures, stop):
                pass
            self.prex, self.prey = x2, y2
        else:
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
