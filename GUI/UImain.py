from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from InterfaceUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


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