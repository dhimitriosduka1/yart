from math import sqrt
from unittest import TestCase

from src.vec3 import Vec3


class TestVec3(TestCase):

    def setUp(self) -> None:
        self.vec: Vec3 = Vec3(2.0, 4.0, 6.0)
        self.other_vec: Vec3 = Vec3(1.0, 2.0, 3.0)
        self.t: float = 2.0

    def test_neg(self):
        vec = -self.vec
        self.assertEqual(vec[0], -2.0)
        self.assertEqual(vec[1], -4.0)
        self.assertEqual(vec[2], -6.0)

    def test_mul(self):
        vec = self.vec * self.t
        self.assertEqual(vec[0], 4.0)
        self.assertEqual(vec[1], 8.0)
        self.assertEqual(vec[2], 12.0)

    def test_add(self):
        vec = self.vec + self.other_vec
        self.assertEqual(vec[0], 3.0)
        self.assertEqual(vec[1], 6.0)
        self.assertEqual(vec[2], 9.0)

    def test_true_div(self):
        vec = self.vec / self.t
        self.assertEqual(vec[0], 1.0)
        self.assertEqual(vec[1], 2.0)
        self.assertEqual(vec[2], 3.0)

    def test_length(self):
        length = self.vec.length()
        self.assertEqual(length, sqrt(56))

    def test_length_squared(self):
        length_squared = self.vec.length_squared()
        self.assertEqual(length_squared, 56)
