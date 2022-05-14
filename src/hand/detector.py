from src.hand.finger import *
import mediapipe as mp
import cv2


class HandDetector:

    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):

        self.state = None
        self.lms = None
        self.processResults = None

        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,
                                        self.maxHands,
                                        self.modelComplexity,
                                        self.detectionCon,
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    # draw the image myHand
    def drawHands(self, img, draw=True):
        self.processResults = self.hands.process(img)

        if self.processResults.multi_hand_landmarks:
            for handLms in self.processResults.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def getPosition(self, img, handNo=0, draw=True, radius=15, color=(255, 0, 255)):
        if self.processResults is None:
            self.processResults = self.hands.process(img)
        self.lms = []

        if self.processResults.multi_hand_landmarks:
            myHand = self.processResults.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lms.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), radius, color, cv2.FILLED)

        return self.lms

    def getFigures(self):
        curveList = []
        if len(self.lms) != 0:
            for i in range(0, 5):
                if self.judgeCurve(i):
                    curveList.append(0)
                else:
                    curveList.append(1)
        return curveList

        # 判断某根手指是否折叠
    def judgeCurve(self, figure, handNo="right"):
        var = fingerMap.get(figure)
        if figure == 0:
            if handNo == "left" and self.lms[var][1] < self.lms[var - 1][1]:
                return True
            elif handNo == "right" and self.lms[var][1] > self.lms[var - 1][1]:
                return True
            return False
        elif self.lms[var][2] > self.lms[var - 2][2]:
            return True
        return False

    def getFirst(self):
        return self.lms[fingerMap.get(Finger.First)]

    def getSecond(self):
        return self.lms[fingerMap.get(Finger.Second)]

    def getThird(self):
        return self.lms[fingerMap.get(Finger.Third)]

    def getFourth(self):
        return self.lms[fingerMap.get(Finger.Fourth)]

    def getFifth(self):
        return self.lms[fingerMap.get(Finger.Fifth)]
