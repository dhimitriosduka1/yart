from src.hittable.hit_record import HitRecord
from src.hittable.hittable import Hittable
from src.ray import Ray
from src.vec3 import Vec3
from math import sqrt


class Sphere(Hittable):

    def __init__(self, center: Vec3, radius: float):
        self.center: Vec3 = center
        self.radius: float = radius

    def hit(self, ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        oc = ray.origin - self.center
        a = ray.direction.length_squared()
        b = 2.0 * Vec3.dot(oc, ray.direction)
        c = oc.length_squared() - self.radius * self.radius
        discriminant = (b * b - 4 * a * c)

        if discriminant < 0.0:
            return False

        discriminant_sqrt = sqrt(discriminant)
        roots = [(-b - discriminant_sqrt) / (2.0 * a), (-b + discriminant_sqrt) / (2.0 * a)]
        root = min(roots)

        if root < t_min or root > t_max:
            return False

        hit_record.t = root
        hit_record.point = ray.at(root)
        outward_normal = (hit_record.point - self.center) / self.radius
        hit_record.set_face_normal(ray, outward_normal)

        return True
