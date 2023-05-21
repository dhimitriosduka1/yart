from src.hittable.hit_record import HitRecord
from src.hittable.hittable import Hittable
from src.ray import Ray


class HittableList(Hittable):

    def __init__(self):
        self.objects: [Hittable] = []

    def add(self, hittable: Hittable):
        self.objects.append(hittable)

    def clear(self):
        self.objects = []

    def hit(self, ray: Ray, t_min: float, t_max: float) -> [Hittable, None]:
        result = None
        closest_so_far = t_max

        for obj in self.objects:
            hit_record = obj.hit(ray, t_min, closest_so_far)
            if hit_record is not None:
                result = hit_record
                closest_so_far = hit_record.t

        return result
