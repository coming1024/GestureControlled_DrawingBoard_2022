import numpy as np

from src.common.constant import *


class DrawPen:
    def __init__(self, color, thickness):
        self.penColor = color
        self.penThickness = thickness


IMG_CANVAS = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
<<<<<<< HEAD
<<<<<<< Updated upstream
PEN = DrawPen(color=PURPLE, thickness=PenThickness)
=======
PEN = DrawPen(color=YELLOW, thickness=PenThickness)
>>>>>>> Stashed changes
=======
PEN = DrawPen(color=PURPLE, thickness=PenThickness)
>>>>>>> 5643444fe1acc420827d1b1049c248bb2c5e2be3
