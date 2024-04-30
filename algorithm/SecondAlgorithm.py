import time


from classes.RectClass import Rectangle, Point
from classes.FunctionClass import Compress, compressCord, find
import numpy


def createMap(rectangles: list[Rectangle], compress: Compress):
    cordMap = numpy.zeros((len(compress.y), len(compress.x)), dtype=int)
    for rect in rectangles:
        for i in range(compress.y.index(rect.y1), compress.y.index(rect.y2)):
            for j in range(compress.x.index(rect.x1), compress.x.index(rect.x2)):
                cordMap[i][j] += 1
    return cordMap


def algorithm(rectangles: list[Rectangle], point: list[Point], count_rec, count_point):
    res = []
    if not rectangles:
        for _ in point:
            res.append(0)
        return res
    prepare_time1 = time.time()
    compress = Compress(*compressCord(rectangles))
    cordMap = createMap(rectangles, compress)
    prepare_time2 = time.time() - prepare_time1
    request_time1 = time.time()
    for p in point:
        ans = 0
        if compress.x[0] <= p.x < compress.x[-1] or compress.y[0] <= p.y < compress.y[-1]:
            ans = cordMap[find(compress.y, p.y)][find(compress.x, p.x)]
        res.append(ans)
    request_time2 = time.time() - request_time1
    with open("time2.txt", "a") as file:
        file.write("{}, {}, {}\n"
                   .format(prepare_time2, request_time2, request_time2 + prepare_time2))
    return res
