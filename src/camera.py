from src.ray import Ray
from src.vec3 import Vec3


class Camera:
    def __init__(self):
        aspect_ration = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = viewport_height * aspect_ration
        focal_length = 1.0

        self.origin = Vec3(0.0, 0.0, 0.0)
        self.horizontal = Vec3(viewport_width, 0.0, 0.0)
        self.vertical = Vec3(0.0, viewport_height, 0.0)
        self.lower_left_corner = self.origin - (self.horizontal / 2) - (self.vertical / 2) - Vec3(0.0, 0.0,
                                                                                                  focal_length)

    def get_ray(self, u: float, v: float) -> Ray:
        return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)
