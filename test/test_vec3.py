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

    def test_sub_number(self):
        vec = self.vec - self.t
        self.assertEqual(vec[0], 0.0)
        self.assertEqual(vec[1], 2.0)
        self.assertEqual(vec[2], 4.0)

    def test_sub_vec(self):
        vec = self.vec - self.other_vec
        self.assertEqual(vec[0], 1.0)
        self.assertEqual(vec[1], 2.0)
        self.assertEqual(vec[2], 3.0)

    def test_mul_number_right(self):
        vec = self.vec * self.t
        self.assertEqual(vec[0], 4.0)
        self.assertEqual(vec[1], 8.0)
        self.assertEqual(vec[2], 12.0)

    def test_mul_number_left(self):
        vec = self.t * self.vec
        self.assertEqual(vec[0], 4.0)
        self.assertEqual(vec[1], 8.0)
        self.assertEqual(vec[2], 12.0)

    def test_mul_vec(self):
        vec = self.vec * self.other_vec
        self.assertEqual(vec[0], 2.0)
        self.assertEqual(vec[1], 8.0)
        self.assertEqual(vec[2], 18.0)

    def test_add_vec(self):
        vec = self.vec + self.other_vec
        self.assertEqual(vec[0], 3.0)
        self.assertEqual(vec[1], 6.0)
        self.assertEqual(vec[2], 9.0)

    def test_add_number(self):
        vec = self.vec + self.t
        self.assertEqual(vec[0], 4.0)
        self.assertEqual(vec[1], 6.0)
        self.assertEqual(vec[2], 8.0)

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

    def test_dot(self):
        dot = Vec3.dot(self.vec, self.other_vec)
        self.assertEqual(dot, 28)

    def test_cross(self):
        cross = Vec3.cross(self.vec, self.other_vec)
        self.assertEqual(cross[0], 0)
        self.assertEqual(cross[1], 0)
        self.assertEqual(cross[2], 0)

    def test_unit_vector(self):
        cross = Vec3.unit_vector(self.vec)
        self.assertEqual(cross[0], 2.0 / sqrt(56))
        self.assertEqual(cross[1], 4.0 / sqrt(56))
        self.assertEqual(cross[2], 6.0 / sqrt(56))
