from src.vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin: Vec3 = origin
        self.direction: Vec3 = direction

    def origin(self) -> Vec3:
        return self.origin

    def direction(self) -> Vec3:
        return self.direction

    def at(self, t):
        return self.origin + t * self.direction

    def __str__(self):
        return f"{self.origin:} {self.direction:}"
