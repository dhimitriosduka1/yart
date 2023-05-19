from math import sqrt


class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def length(self):
        return sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __add__(self, other):
        self.e[0] += other[0]
        self.e[1] += other[1]
        self.e[2] += other[2]
        return self

    def __mul__(self, other):
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __truediv__(self, other):
        return self * (1 / other)

    def __getitem__(self, item):
        return self.e[item]
