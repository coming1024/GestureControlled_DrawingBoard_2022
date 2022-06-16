from abc import abstractmethod
from src.hand.finger import fingerMap, Finger


class HandTag:
    RIGHT = "right"
    LEFT = "left"


# 判断是左手还是右手,现在是用大拇指来作为区分
def judgeHand(myHand, imgWidth, imgHeight):
    firstFinger = None
    fifthFinger = None
    result = []
    for id, lm in enumerate(myHand.landmark):
        if id == 2:
            firstFinger = lm.x
        if id == 17:
            fifthFinger = lm.x
        cx, cy = int(lm.x * imgWidth), int(lm.y * imgHeight)
        result.append([id, cx, cy])
    if firstFinger < fifthFinger:
        return HandTag.RIGHT, result
    return HandTag.LEFT, result


class Hand:
    FirstFlag = 0
    SecondFlag = 0

    def __init__(self):
        self.tag = None
        self.lms = None

    @classmethod
    def firstFlag(cls):
        return cls.FirstFlag

    @classmethod
    def secondFlag(cls):
        return cls.SecondFlag

    def getFingers(self):
        curveList = []
        if self.lms is not None and len(self.lms) != 0:
            for i in range(0, 5):
                if self.judgeCurve(i):
                    curveList.append(0)
                else:
                    curveList.append(1)
        return curveList

    # 判断某根手指是否完全
    @abstractmethod
    def judgeCurve(self, finger):
        pass

    # 每只手的流程
    @abstractmethod
    def process(self, img, hand, mainWindow=None):
        pass

    # 判断手是否出现在画面上
    def judgeNull(self):
        fingers = self.getFingers()
        return fingers is None or len(fingers) == 0

    def getOneFinger(self, fingerNo):
        return self.lms[fingerNo]

    def getFirst(self):
        return self.getOneFinger(fingerMap.get(Finger.First))

    def getSecond(self):
        return self.getOneFinger(fingerMap.get(Finger.Second))

    def getThird(self):
        return self.getOneFinger(fingerMap.get(Finger.Third))

    def getFourth(self):
        return self.getOneFinger(fingerMap.get(Finger.Fourth))

    def getFifth(self):
        return self.getOneFinger(fingerMap.get(Finger.Fifth))
