from InterfaceUI import *
from BtnFunction.BtnFunction import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
# 3
global Templ_Change
Templ_Change = 0
# 3
class PaintWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute((QtCore.Qt.WA_TranslucentBackground))
        # %
        # self.setupUi(self)
        # BtnFunction.PreParement(self)
        # BtnFunction.UiShaw(self)
        # %
        self.show()

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

    # 放大缩小（还有问题）
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/maxsize.png"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/minimizeWhite.png"))
    # 浮窗（尚有问题）
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PaintWindow()
    sys.exit(app.exec_())