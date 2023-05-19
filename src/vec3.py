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

    @staticmethod
    def dot(u, v):
        return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

    @staticmethod
    def cross(u, v):
        return Vec3(
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]
        )

    @staticmethod
    def unit_vector(u):
        return u / u.length()

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] - other[0], self.e[1] - other[1], self.e[2] - other[2])
        self.e[0] -= other
        self.e[1] -= other
        self.e[2] -= other
        return self

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] + other[0], self.e[1] + other[1], self.e[2] + other[2])
        self.e[0] += other
        self.e[1] += other
        self.e[2] += other
        return self

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] * other[0], self.e[1] * other[1], self.e[2] * other[2])
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __rmul__(self, other):
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __truediv__(self, other):
        return self * (1 / other)

    def __getitem__(self, item):
        return self.e[item]

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"
