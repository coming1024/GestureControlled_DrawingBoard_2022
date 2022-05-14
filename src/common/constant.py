import cv2
import numpy as np
from src.common.pen import DrawPen
from src.hand import detector


PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

PenThickness = 10
PenRadius = 15
eraseThickness = 30

IMG_HEIGHT = 720
IMG_WIDTH = 1280

CAP = cv2.VideoCapture(0)
CAP.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
CAP.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
HAND = detector.HandDetector(detectionCon=0.8, trackCon=0.8)
IMG_CANVAS = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
PEN = DrawPen(color=PURPLE,thickness=PenThickness)

