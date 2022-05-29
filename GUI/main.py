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
        self.pushButton_4.clicked.connect(self.penBoardShow)
        self.pushButton_15.clicked.connect(self.penBoardHide)
        self.shapeBoardHide()
        self.pushButton_6.clicked.connect(self.shapeBoardShow)
        self.pushButton_14.clicked.connect(self.shapeBoardHide)
        self.colorBoardHide()
        self.pushButton_16.clicked.connect(self.colorBoardShow)
        self.pushButton_13.clicked.connect(self.colorBoardHide)
        BtnFunction.PreParement(self)
        BtnFunction.UiShaw(self)
        self.show()


    # 拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.QtWidgetsm_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 放大缩小（还有问题）
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/maxsize.png"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/minimizeWhite.png"))

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

    # 形状隐藏
    def shapeBoardHide(self):
        self.frame_6.setVisible(False)

    # 形状展示
    def shapeBoardShow(self):
        self.frame_5.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_6.setVisible(True)

    # 颜色隐藏
    def colorBoardHide(self):
        self.frame_8.setVisible(False)

    # 颜色展示
    def colorBoardShow(self):
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_8.setVisible(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = PaintWindow()
    sys.exit(app.exec_())