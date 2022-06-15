import math

import cv2
import numpy as np

from src.common.base import PEN


def getMidPoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def getMidPoint(point1, point2):
    return getMidPoint(point1.x, point1.y, point2.x, point2.y)


def drawRectangle(img, row, col, length, width, angle):
    angle *= (10 / 180) * math.pi  # 弧度

    xo = np.cos(angle)
    yo = np.sin(angle)

    y1 = row + length / 2 * yo
    x1 = col - length / 2 * xo
    y2 = row - width / 2 * yo
    x2 = col + width / 2 * xo

    array = np.array(
        [
            [y1 - width / 2 * xo, x1 - width / 2 * yo],
            [y2 - width / 2 * xo, x2 - width / 2 * yo],
            [y2 + width / 2 * xo, x2 + width / 2 * yo],
            [y1 + width / 2 * xo, x1 + width / 2 * yo],
        ])

    cv2.rectangle(img, array[1], array[3], PEN.penColor, PEN.penThickness)

def drawCircle(img, row, col, radius):
    cv2.circle(img,(row,col),radius,PEN.penColor,PEN.penThickness)

def drawTriangle(img, point1, point2, point3, penColor, thickness=10):
    cv2.line(img, point1, point2, penColor, thickness)
    cv2.line(img, point2, point3, penColor, thickness)
    cv2.line(img, point1, point3, penColor, thickness)
