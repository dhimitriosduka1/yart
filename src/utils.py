import random
from math import sqrt

from src.constants import PI, INFINITY
from src.hittable.hit_record import HitRecord
from src.hittable.hittable import Hittable
from src.ray import Ray
from src.vec3 import Vec3


def write_ppm(data, rows, cols, path, sample_per_pixel):
    with open(path, "w") as image:
        image.write("P3\n")
        image.write(f"{rows} {cols}\n")
        image.write("255\n")

        for color in data:
            write_color(color, image, sample_per_pixel)


def write_color(color: Vec3, stream, sample_per_pixel: int):
    components = [color.x(), color.y(), color.z()]
    scale = 1.0 / sample_per_pixel
    components = list(map(lambda c: 256 * (clamp(c * scale, 0.0, 0.999)), components))
    stream.write(f"{int(components[0])} {int(components[1])} {int(components[2])}\n")


def hit_sphere(center: Vec3, radius: float, ray: Ray):
    oc = ray.origin - center
    a = ray.direction.length_squared()
    b = 2.0 * Vec3.dot(oc, ray.direction)
    c = oc.length_squared() - radius * radius
    discriminant = (b * b - 4 * a * c)
    return -1.0 if discriminant < 0 else ((-b - sqrt(discriminant)) / (2.0 * a))


def ray_color(ray: Ray, world: Hittable, depth: int):
    if depth <= 0:
        return Vec3()
    hit_record: HitRecord = world.hit(ray, 0, INFINITY)
    if hit_record is not None:
        target = hit_record.point + hit_record.normal + random_in_unit_sphere()
        return 0.5 * ray_color(Ray(hit_record.point, target - hit_record.point), world, depth - 1)
    unit_direction: Vec3 = Vec3.unit_vector(ray.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def degrees_to_radians(degrees: float):
    return degrees * PI / 180.0


def random_float():
    return random.Random().random()


def random_float_with_constraints(lower: float, upper: float):
    return lower + (upper - lower) * random.Random().random()


def random_in_unit_sphere():
    while True:
        random_vector = random_vec_with_constraints(-1, 1)
        if random_vector.length() < 1:
            return random_vector


def random_vec():
    return Vec3(random_float(), random_float(), random_float())


def random_vec_with_constraints(lower: float, upper: float):
    return Vec3(random_float_with_constraints(lower, upper),
                random_float_with_constraints(lower, upper),
                random_float_with_constraints(lower, upper))


def clamp(x: float, lower: float, upper: float) -> float:
    if x < lower:
        return lower
    if x > upper:
        return upper
    return x
