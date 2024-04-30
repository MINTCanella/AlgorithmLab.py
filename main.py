import random

from classes.RectClass import Rectangle, Point
from algorithm import FirstAlgorithm as First
from algorithm import SecondAlgorithm as Second
from algorithm import ThirdAlgorithm as Third

'''
rect = []
point = []

n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rect.append(Rectangle(x1, y1, x2, y2))

m = int(input())
for i in range(m):
    x, y = map(float, input().split(" "))
    point.append(Point(x, y))
'''
'''
rect = []
point = []
ans1 = []
ans2 = []
ans3 = []
find = 0
while ans1 == ans2 == ans3:
    find += 1
    print(find)
    for i in range(random.randint(0, 20)):
        x1 = random.randint(0, 100)
        y1 = random.randint(0, 100)
        x2 = x1 + random.randint(1, 100)
        y2 = x2 + random.randint(1, 100)
        rect.append(Rectangle(x1, y1, x2, y2))

    for i in range(random.randint(0, 30)):
        x = random.randint(-3, 120)
        y = random.randint(-3, 120)
        point.append(Point(x, y))
    ans1 = First.algorithm(rect, point)
    ans2 = Second.algorithm(rect, point)
    ans3 = Third.algorithm(rect, point)

print(rect, point, ans1, ans2, ans3)
'''
n = []
m = []
p1 = 2053
p2 = 1579
for i in range(5, 11):
    n.append(2 ** i)
for i in range(4, 13):
    m.append(2 ** i)
for count_rect in n:
    rect = []
    for i in range(count_rect):
        rect.append(Rectangle(10 * i, 10 * i, 10 * (2 * count_rect - 1), 10 * (2 * count_rect - 1)))
    for count_point in m:
        point = []
        for i in range(count_rect):
            point.append(Point((p1 * i) ^ 31 % (20 * count_rect), (p2 * i) ^ 31 % (20 * count_rect)))
        First.algorithm(rect, point, count_rect, count_point)
        #Second.algorithm(rect, point, count_rect, count_point)
        Third.algorithm(rect, point, count_rect, count_point)
