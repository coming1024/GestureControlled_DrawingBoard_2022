from PyQt5 import QtCore, QtWidgets, QtGui

from src.ui.InterfaceUI_01 import *

global Templ_Expend
Templ_Expend = 0

class BtnFunction(Ui_MainWindow):
    def UiShaw(self):
        # 滑动模块阴影
        self.Meau_WT.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect
            (blurRadius=40, xOffset=10, yOffset=10, color=QtGui.QColor(0, 0, 0)))
        # self.Title.setGraphicsEffect(
        #     QtWidgets.QGraphicsDropShadowEffect
        #     (blurRadius=0, xOffset=1, yOffset=1, color=QtGui.QColor(0, 0, 0)))

    def PreParement(self):
        self.Meau_WT.hide()
        self.TarGet = self.Meau_WT
        self._animation = QtCore.QPropertyAnimation(self.TarGet)
        self._animation.setTargetObject(self.TarGet)
        self._animation.setPropertyName(b"geometry")
        self._animation.setDuration(500)
        self._animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)

    def MeauExpend(self):
        global Templ_Expend
        if Templ_Expend == 0:
            self.Meau_WT.show()
            self._animation.setStartValue(QtCore.QRect(self.TarGet.x(), self.TarGet.y(), 0, self.TarGet.height()))
            self._animation.setEndValue((QtCore.QRect(self.TarGet.x(), self.TarGet.y(), 150, self.TarGet.height())))
            self._animation.start()
            Templ_Expend = 1
            return
        if Templ_Expend == 1:
            self.Meau_WT.show()
            self._animation.setStartValue((QtCore.QRect(self.TarGet.x(), self.TarGet.y(), 150, self.TarGet.height())))
            self._animation.setEndValue(QtCore.QRect(self.TarGet.x(), self.TarGet.y(), 0, self.TarGet.height()))
            self._animation.start()

            Templ_Expend = 0
            return


