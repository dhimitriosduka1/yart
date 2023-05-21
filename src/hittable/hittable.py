from abc import ABC, abstractmethod

from src.hittable.hit_record import HitRecord
from src.ray import Ray


class Hittable(ABC):

    @abstractmethod
    def hit(self, ray: Ray, t_min: float, t_max: float) -> [HitRecord, None]:
        pass
