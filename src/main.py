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
from src.ui.InterfaceUI_01 import *

CAP = cv2.VideoCapture(0)
CAP.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
CAP.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
HAND_DETECTOR = detector.HandDetector(detectionCon=0.8, trackCon=0.8)

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

    def draw(self):
        success, img = imgInit()

        leftHand=HAND_DETECTOR.leftHand
        rightHand=HAND_DETECTOR.rightHand
        leftHand.process(img,rightHand,self)
        rightHand.process(img,leftHand)

        img = detectorImage(img, IMG_CANVAS)
        showImage=QImage(img.data,img.shape[1],img.shape[0],QImage.Format_BGR888)
        # showImage = QImage(IMG_CANVAS.data, IMG_CANVAS.shape[1], IMG_CANVAS.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))  # 将摄像头显示在之前创建的Label控件中
        # self.timer_camera.start(1)
        # cv2.imshow("Img", img)
        cv2.imshow("canvas", IMG_CANVAS)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
