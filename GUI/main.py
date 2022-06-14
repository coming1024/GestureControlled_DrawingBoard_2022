from InterfaceUI_01 import *
from BtnFunction.BtnFunction import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

global Templ_Change
Templ_Change = 0

class PaintWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute((QtCore.Qt.WA_TranslucentBackground))
        self.penBoardHide()
        self.pushButton_4.clicked.connect(self.penBoardShow)       # 点击画笔按钮
        self.pushButton_15.clicked.connect(self.penBoardHide)       # 隐藏画笔菜单
        self.shapeBoardHide()
        self.pushButton_6.clicked.connect(self.shapeBoardShow)       # 点击形状按钮
        self.pushButton_14.clicked.connect(self.shapeBoardHide)       # 隐藏形状菜单
        self.colorBoardHide()
        self.pushButton_16.clicked.connect(self.colorBoardShow)       # 点击颜色按钮
        self.pushButton_13.clicked.connect(self.colorBoardHide)       # 隐藏形状菜单
        self.pushButton_5.clicked.connect(self.eraserBtn)       # 点击橡皮按钮
        self.pushButton_9.clicked.connect(self.saveBtn)        # 点击保存按钮
        self.pushButton_7.clicked.connect(self.newBtn)         # 点击新建按钮
        BtnFunction.PreParement(self)
        BtnFunction.UiShaw(self)
        self.show()

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
        self.btnColorBack()

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
        self.btnColorBack()

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
        self.btnColorBack()

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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = PaintWindow()
    sys.exit(app.exec_())