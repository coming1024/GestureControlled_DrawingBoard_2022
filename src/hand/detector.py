import mediapipe as mp

from src.hand.hand import *
from src.hand.leftHand import LeftHand
from src.hand.rightHand import RightHand


class HandDetector:

    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.processResults = None
        self.leftHand = LeftHand()
        self.rightHand = RightHand()

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

    def drawHands(self, img, draw=True):
        self.processResults = self.hands.process(img)

        if self.processResults.multi_hand_landmarks:
            for handLms in self.processResults.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def initPosition(self, img):
        if self.processResults is None:
            self.processResults = self.hands.process(img)

        h, w, c = img.shape
        pResult = self.processResults
        if pResult.multi_hand_landmarks:
            for myHand in pResult.multi_hand_landmarks:
                handNo, result = judgeHand(myHand, w, h)
                if handNo == HandTag.LEFT:
                    self.leftHand.lms = result
                else:
                    self.rightHand.lms = result

    # def getPosition(self, img, handNo=0, draw=True, radius=15, color=PURPLE):
    #     if self.processResults is None:
    #         self.processResults = self.hands.process(img)
    #
    #     h, w, c = img.shape
    #
    #     self.leftLandMark=[]
    #     self.rightLandMark=[]
    #
    #     pResult=self.processResults
    #     if pResult.multi_hand_landmarks:
    #         for judgeHand in pResult.multi_handedness:
    #             result = str(judgeHand).split("\n")
    #             index= int(result[1].split(":")[1].strip())
    #             label =result[3].split(":")[1].strip()
    #             print(index,label)
    #             if len(pResult.multi_hand_landmarks)>index:
    #                 myHand = pResult.multi_hand_landmarks[index]
    #                 for id, lm in enumerate(myHand.landmark):
    #                     cx, cy = int(lm.x * w), int(lm.y * h)
    #                     if label == "Left":
    #                         self.leftLandMark.append([id, cx, cy])
    #                     else:
    #                         self.rightLandMark.append([id, cx, cy])
    #                     if draw:
    #                         cv2.circle(img, (cx, cy), radius, color, cv2.FILLED)
    #     return self.rightLandMark
