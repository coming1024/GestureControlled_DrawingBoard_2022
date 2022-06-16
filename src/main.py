import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

from src.common.base import IMG_CANVAS
from src.common.constant import IMG_HEIGHT, IMG_WIDTH, OpenPath
from src.hand import detector
from src.image.detector import reverseImage, detectorImage
from src.image.draw import *
from src.ui.BtnFunction.BtnFunction import *
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


class PaintWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    select_Pen_flag = False

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
        # BtnFunction.PreParement(self)
        # BtnFunction.UiShaw(self)
        self.initBtn()
        self.show()
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.draw)
        self.timer_camera.start(5)

    def draw(self):
        success, img = imgInit()

        leftHand = HAND_DETECTOR.leftHand
        rightHand = HAND_DETECTOR.rightHand
        # IMG_CANVAS = cv2.imread(OpenPath)
        leftHand.process(img, rightHand, self)
        rightHand.process(img, leftHand, self)

        detectorImage(img, IMG_CANVAS)
        showImage = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888)
        # showImage = QImage(IMG_CANVAS.data, IMG_CANVAS.shape[1], IMG_CANVAS.shape[0], QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(showImage))  # 将摄像头显示在之前创建的Label控件中
        # self.timer_camera.start(1)
        # cv2.imshow("Img", img)
        cv2.imshow("canvas", IMG_CANVAS)

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

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

    # 隐藏橡皮
    def closeEraser(self):
        self.frame_5.setVisible(False)

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

    # 点击打开
    def newOpen(self):
        self.btnColorBack()
        self.pushButton_8.setStyleSheet("QPushButton{\n"
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

    # 按钮初始化
    def initBtn(self):
        self.pushButton_10.clicked.connect(self.selectBtn10)  # 粗细1
        self.pushButton_11.clicked.connect(self.selectBtn11)  # 粗细2
        self.pushButton_12.clicked.connect(self.selectBtn12)  # 粗细3
        self.pushButton_21.clicked.connect(self.selectBtn21)  # 形状1
        self.pushButton_22.clicked.connect(self.selectBtn22)
        self.pushButton_23.clicked.connect(self.selectBtn23)
        self.pushButton_24.clicked.connect(self.selectBtn24)
        self.pushButton_25.clicked.connect(self.selectBtn25)
        self.pushButton_26.clicked.connect(self.selectBtn26)
        self.pushButton_27.clicked.connect(self.selectBtn27)
        self.pushButton_28.clicked.connect(self.selectBtn28)
        self.pushButton_29.clicked.connect(self.selectBtn29)
        self.pushButton_30.clicked.connect(self.selectBtn30)
        self.pushButton_31.clicked.connect(self.selectBtn31)

    # 其他点击改按钮颜色
    def selectBtn10(self):
        self.secondBtnBack()
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn11(self):
        self.secondBtnBack()
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn12(self):
        self.secondBtnBack()
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn21(self):
        self.secondBtnBack()
        self.pushButton_21.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn22(self):
        self.secondBtnBack()
        self.pushButton_22.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn23(self):
        self.secondBtnBack()
        self.pushButton_23.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn24(self):
        self.secondBtnBack()
        self.pushButton_24.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn25(self):
        self.secondBtnBack()
        self.pushButton_25.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn26(self):
        self.secondBtnBack()
        self.pushButton_26.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn27(self):
        self.secondBtnBack()
        self.pushButton_27.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn28(self):
        self.secondBtnBack()
        self.pushButton_28.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn29(self):
        self.secondBtnBack()
        self.pushButton_29.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn30(self):
        self.secondBtnBack()
        self.pushButton_30.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def selectBtn31(self):
        self.secondBtnBack()
        self.pushButton_31.setStyleSheet("QPushButton{\n"
                                         "    border-left:7px solid #ffd194;\n"
                                         "    border-radius:9px;\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}\n")

    def chooseLabel(self, str):
        self.label_4.setText(str)

    # 恢复按钮颜色
    def secondBtnBack(self):
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_21.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_22.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_23.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_24.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_25.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_26.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_27.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_28.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_29.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_30.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_31.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_32.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_33.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")
        self.pushButton_34.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(242, 242, 242);\n"
                                         "margin-left:10px;\n"
                                         "margin-right:10px;\n"
                                         "border-radius:10px;\n"
                                         "}")


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    # global UI
    UI = PaintWindow()
    UI.show()

    sys.exit(app.exec_())
