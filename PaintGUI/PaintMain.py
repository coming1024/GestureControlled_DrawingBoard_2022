from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
from PaintGUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    tool=0
    pen=1
    color=1
    shape=0
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.__InitView()
        self.setColor()

    def __InitView(self):
        self.toolButton_2 = QPushButton(self)
        self.toolButton_2.setText('画笔')
        self.toolButton_2.setGeometry(692, 0, 331, 121)
        self.toolButton_2.clicked.connect(self.clickButton)
        self.toolButton_4 = QPushButton(self)
        self.toolButton_4.setText('图形')
        self.toolButton_4.setGeometry(1352, 0, 281, 121)
        self.toolButton_4.clicked.connect(self.clickButton1)
        self.toolButton_5 = QToolButton(self)
        self.toolButton_5.setText('画笔种类1')
        self.toolButton_5.setGeometry(40, 30, 100, 100)
        self.toolButton_5.setVisible(False)
        # self.toolButton_5.clicked.connect(self.clickPen1)
        self.toolButton_6 = QToolButton(self)
        self.toolButton_6.setText('画笔种类2')
        self.toolButton_6.setGeometry(40, 200, 100, 100)
        self.toolButton_6.setVisible(False)
        # self.toolButton_6.clicked.connect(self.clickPen2)
        self.toolButton_9 = QToolButton(self)
        self.toolButton_9.setText('三角形')
        self.toolButton_9.setGeometry(50, 60, 100, 100)
        self.toolButton_9.setVisible(False)
        # self.toolButton_9.clicked.connect(self.clickShape1)
        self.toolButton_10 = QToolButton(self)
        self.toolButton_10.setText('长方形')
        self.toolButton_10.setGeometry(50, 300, 100, 100)
        self.toolButton_10.setVisible(False)
        # self.toolButton_10.clicked.connect(self.clickShape2)
        self.toolButton_22.clicked.connect(self.clickButton2)
        self.toolButton_25.setVisible(False)
        self.toolButton_26.setVisible(False)
        self.toolButton_27.setVisible(False)

    def __InitPen(self): # 展示画笔选择
        self.toolButton_9.setVisible(False)
        self.toolButton_10.setVisible(False)
        self.toolButton_5.setVisible(True)
        self.toolButton_6.setVisible(True)
        self.toolButton_25.setVisible(False)
        self.toolButton_26.setVisible(False)
        self.toolButton_27.setVisible(False)

    def __InitShape(self): # 展示形状选择
        self.toolButton_5.setVisible(False)
        self.toolButton_6.setVisible(False)
        self.toolButton_9.setVisible(True)
        self.toolButton_10.setVisible(True)
        self.toolButton_25.setVisible(False)
        self.toolButton_26.setVisible(False)
        self.toolButton_27.setVisible(False)

    def __InitColor(self): # 展示颜色选择
        self.toolButton_5.setVisible(False)
        self.toolButton_6.setVisible(False)
        self.toolButton_9.setVisible(False)
        self.toolButton_10.setVisible(False)
        self.toolButton_25.setVisible(True)
        self.toolButton_26.setVisible(True)
        self.toolButton_27.setVisible(True)

    def setColor(self):
        self.toolButton_2.setStyleSheet("QPushButton{background:#e1e1e1;}")
        self.toolButton_4.setStyleSheet("QPushButton{background:#e1e1e1;}")

    def clickButton(self):  # 点击画笔
        self.__InitPen()
        self.setColor()
        self.toolButton_2.setStyleSheet("QPushButton{background:#f0f0f0;}")
        # sender = self.sender()
        # print(sender.text() + '被点击')

    def clickButton1(self): # 点击形状
        self.__InitShape()
        self.setColor()
        self.toolButton_4.setStyleSheet("QPushButton{background:#f0f0f0;}")
        # sender = self.sender()
        # print(sender.text() + '被点击')

    def clickButton2(self): # 点击颜色
        self.__InitColor()
        self.setColor()
        self.toolButton_22.setStyleSheet("QPushButton{background:#f0f0f0;}")

    # def clickPen1(self):
    #     self.setColor()
    #     self.toolButton_5.setStyleSheet("QPushButton{background:#f0f0f0;}")
    #     sender = self.sender()
    #     print(sender.text() + '被点击')
    # 
    # def clickPen2(self):
    #     self.setColor()
    #     self.toolButton_6.setStyleSheet("QPushButton{background:#f0f0f0;}")
    #     sender = self.sender()
    #     print(sender.text() + '被点击')
    # 
    # def clickShape1(self):
    #     self.setColor()
    #     self.toolButton_9.setStyleSheet("QPushButton{background:#f0f0f0;}")
    #     sender = self.sender()
    #     print(sender.text() + '被点击')
    # 
    # def clickShape2(self):
    #     self.setColor()
    #     self.toolButton_10.setStyleSheet("QPushButton{background:#f0f0f0;}")
    #     sender = self.sender()
    #     print(sender.text() + '被点击')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()    # 实例化我们定义好的窗口类对象
    # styleFile = './style.qss'
    # # 换肤时进行全局修改，只需要修改不同的QSS文件即可
    # style = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(style)
    window.show()
    # window.showMaximized()    # 用来显示我们写好的Gui界面
    sys.exit(app.exec_())     # sys.exit()表示退出程序操作，app.exec_()类似于tkinter模块中定义Gui界面时进行的Mainloop()，
                              # 即开始执行主循环体，配合sys.exit()退出命令可以在我们退出程序时清空内存，达到洁净模式。