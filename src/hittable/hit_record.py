from src.ray import Ray
from src.vec3 import Vec3


class HitRecord:
    def __init__(self, point: Vec3 = Vec3(), normal: Vec3 = Vec3(), t: float = 0.0, front_face: bool = False):
        self.point = point
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, ray: Ray, outward_normal: Vec3):
        front_face = Vec3.dot(ray.direction, outward_normal) < 0.0
        self.normal = outward_normal if front_face else -outward_normal
