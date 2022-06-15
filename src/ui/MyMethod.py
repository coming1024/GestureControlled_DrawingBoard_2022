from src.main import PaintWindow


def penBoardShow(UI):
    UI.frame_6.setVisible(False)
    UI.frame_8.setVisible(False)
    UI.frame_5.setVisible(True)
    UI.btnColorBack()
    UI.pushButton_4.setStyleSheet("QPushButton{\n"
                                    "    font: 17pt \"仿宋\";\n"
                                    "    color:rgba(200, 200,200, 255);\n"
                                    "    border-left:7px solid #ffd194;\n"
                                    "    border-radius:9px;\n"
                                    "    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 0))\n"
                                    "}\n")