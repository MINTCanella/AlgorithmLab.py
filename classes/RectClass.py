class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2})"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Interval:
    def __init__(self, y1, y2, end):
        self.y1 = y1
        self.y2 = y2
        self.end = end

    def __repr__(self):
        return f"Interval({self.y1}, {self.y2}, {self.end})"
