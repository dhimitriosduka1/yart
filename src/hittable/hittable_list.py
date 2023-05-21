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

    def hit(self, ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        temp_hit_record: HitRecord = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            if obj.hit(ray, t_min, t_max, temp_hit_record):
                hit_anything = True
                closest_so_far = temp_hit_record.t
                hit_record = temp_hit_record

        return hit_anything
