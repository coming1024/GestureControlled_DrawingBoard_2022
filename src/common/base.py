import numpy as np

from src.common.constant import *


class DrawPen:
    def __init__(self, color, thickness):
        self.penColor = color
        self.penThickness = thickness


IMG_CANVAS = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
PEN = DrawPen(color=PURPLE, thickness=PenThickness)
