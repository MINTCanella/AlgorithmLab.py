import copy
import time

from classes.RectClass import Rectangle, Point, Interval
from classes.FunctionClass import Compress, compressCord, find
from classes.SegmentTree import Node


def createTree(left, right):
    if left > right:
        return None
    if left == right:
        return Node(0, None, None, left, right)
    leftChild = createTree(left, (left + right) // 2)
    rightChild = createTree((left + right) // 2 + 1, right)
    return Node(0, leftChild, rightChild, left, right)


def updateTree(node: Node, left, right, value):
    if node.intervalL == node.intervalR:
        update = copy.copy(node)
        update.value += value
        return update

    conditionL = node.leftChild.intervalL > right or node.leftChild.intervalR < left
    conditionR = node.rightChild.intervalL > right or node.rightChild.intervalR < left

    leftChild = node.leftChild if conditionL else updateTree(node.leftChild, left, right, value)
    rightChild = node.rightChild if conditionR else updateTree(node.rightChild, left, right, value)

    return Node(max(leftChild.value, rightChild.value), leftChild, rightChild, node.intervalL, node.intervalR)


def findInTree(node: Node, value):
    if node.intervalL == node.intervalR and node.intervalL == value:
        return node.value
    if value <= (node.intervalL+node.intervalR)//2:
        ans = findInTree(node.leftChild, value)
    else:
        ans = findInTree(node.rightChild, value)
    return ans


def algorithm(rectangles: list[Rectangle], point: list[Point], count_rec, count_point):
    res = []
    if not rectangles:
        for _ in point:
            res.append(0)
        return res
    prepare_time1 = time.time()
    compress = Compress(*compressCord(rectangles))
    lenCord = len(compress.x)
    ratio = [[] for _ in range(lenCord)]
    roots = [Node(None, None, None, 0, 0)] * (lenCord + 1)
    roots[0] = createTree(0, len(compress.y) - 1)

    for rect in rectangles:
        ratio[find(compress.x, rect.x1)].append(Interval(find(compress.y, rect.y1), find(compress.y, rect.y2) - 1, 1))
        ratio[find(compress.x,rect.x2)].append(Interval(find(compress.y,rect.y1), find(compress.y,rect.y2)-1, -1))

    for i in range(1, lenCord + 1):
        for interval in ratio[i-1]:
            if roots[i].value is None:
                roots[i] = roots[i-1]
            roots[i] = updateTree(roots[i], interval.y1, interval.y2, interval.end)
    prepare_time2 = time.time() - prepare_time1
    request_time1 = time.time()
    for p in point:
        ans = 0
        if compress.x[0] <= p.x < compress.x[-1] or compress.y[0] <= p.y < compress.y[-1]:
            posX = find(compress.x, p.x)
            posY = find(compress.y, p.y)
            ans = findInTree(roots[posX + 1], posY) if posX != -1 and posY != -1 else 0
        res.append(ans)
    request_time2 = time.time() - request_time1
    with open("time3.txt", "a") as file:
        file.write("{}, {},  {}\n".format(prepare_time2*1000, request_time2*1000, (request_time2 + prepare_time2) * 1000))
    return res

