from unittest import TestCase

from src.ray import Ray
from src.vec3 import Vec3


class TestRay(TestCase):

    def setUp(self) -> None:
        self.origin = Vec3(1.0, 2.0, 3.0)
        self.direction = Vec3(2.0, 1.0, 4.0)

        self.ray = Ray(self.origin, self.direction)

        self.t = 2.0

    def test_at(self):
        at = self.ray.at(self.t)
        self.assertEqual(at[0], 5.0)
        self.assertEqual(at[1], 4.0)
        self.assertEqual(at[2], 11.0)
