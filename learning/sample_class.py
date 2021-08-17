from math import pi, sqrt


class Point:
    def __init__(self, x, y, r):
        self._center = {'x': x, 'y': y}
        self._radius = r

    @property
    def area(self):
        return pi * (self._radius ** 2)

    @area.setter
    def area(self, a):
        self._radius = sqrt(a / pi)

    @property
    def radius(self):
        return self._radius


class SuperPoint(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
