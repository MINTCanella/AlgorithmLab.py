from classes.RectClass import Rectangle


class Compress:
    def __init__(self, cordX, cordY):
        self.x = cordX
        self.y = cordY

    def __repr__(self):
        return f"Compress({self.x}, {self.y})"


def compressCord(rectangles: list[Rectangle]):
    compressX = set()
    compressY = set()
    for rect in rectangles:
        compressX.update([rect.x1, rect.x2])
        compressY.update([rect.y1, rect.y2])
    return sorted(list(compressX)), sorted(list(compressY))


def find(compress, cord):
    left = 0
    right = len(compress) - 1
    if cord < compress[0] or cord > compress[-1]: return -1
    while left < right:
        mid = (left+right)//2

        if cord == compress[mid]:

            return mid
        if cord > compress[mid]:
            left = mid + 1
        else:
            right = mid
    if compress[left] == cord:
        return left
    else:
        return left - 1