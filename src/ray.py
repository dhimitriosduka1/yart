from src.vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def origin(self):
        return self.origin

    def direction(self):
        return self.direction

    def at(self, t):
        return self.origin + t * self.direction

    @staticmethod
    def ray_color(ray):
        unit_direction: Vec3 = Vec3.unit_vector(ray.direction)
        t = 0.5 * (unit_direction.y() + 1.0)
        return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)

    def __str__(self):
        return f"{self.origin:} {self.direction:}"
