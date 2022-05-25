import cv2
import numpy as np

from src.common.constant import *
from src.common.pen import DrawPen
from src.hand import detector

CAP = cv2.VideoCapture(0)
CAP.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
CAP.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
HAND_DETECTOR = detector.HandDetector(detectionCon=0.8, trackCon=0.8)
IMG_CANVAS = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
PEN = DrawPen(color=YELLOW, thickness=PenThickness)
