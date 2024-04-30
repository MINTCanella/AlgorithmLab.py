import time
import timeit

from classes.RectClass import Rectangle, Point


def bruteforce(rectangles: list[Rectangle], point: Point):
    p = point
    res = 0
    for r in rectangles:
        if r.x1 <= p.x < r.x2 and r.y1 <= p.y < r.y2:
            res += 1
    return res


def algorithm(rectangles: list[Rectangle], point: list[Point], count_rec, count_point):
    res = []
    request_time1 = time.time()
    for p in point:
        res.append(bruteforce(rectangles, p))
    request_time2 = time.time() - request_time1
    with open("time1.txt", "a") as file:
        file.write("Прямоугольников: {}, Точек: {}, Время: {}\n".format(count_rec, count_point, request_time2*1000))
    return res
