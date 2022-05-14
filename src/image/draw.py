import cv2


def getMidPoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def getMidPoint(point1, point2):
    return getMidPoint(point1.x, point1.y, point2.x, point2.y)


def drawRectangle(img, point1, point2, penColor, thickness=10):
    cv2.rectangle(img, point1, point2, penColor, thickness)


def drawTriangle(img,point1,point2,point3,penColor,thickness=10):
    cv2.line(img,point1,point2,penColor,thickness)
    cv2.line(img,point2,point3,penColor,thickness)
    cv2.line(img,point1,point3,penColor,thickness)




