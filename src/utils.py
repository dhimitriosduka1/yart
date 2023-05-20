from math import sqrt

from src.ray import Ray
from src.vec3 import Vec3


def write_ppm(data, rows, cols, path):
    with open(path, "w") as image:
        image.write("P3\n")
        image.write(f"{rows} {cols}\n")
        image.write("255\n")

        for color in data:
            write_color(color, image)


def write_color(color: Vec3, stream):
    stream.write(f"{int(255.999 * color[0])} {int(255.999 * color[1])} {int(255.999 * color[2])}\n")


def hit_sphere(center: Vec3, radius: float, ray: Ray):
    oc = ray.origin - center
    a = Vec3.dot(ray.direction, ray.direction)
    b = 2.0 * Vec3.dot(oc, ray.direction)
    c = Vec3.dot(oc, oc) - radius * radius
    discriminant = (b * b - 4 * a * c)
    return -1.0 if discriminant < 0 else ((-b - sqrt(discriminant)) / (2.0 * a))


def ray_color(ray: Ray):
    t = hit_sphere(Vec3(0.0, 0.0, -1.0), 0.5, ray)
    if t > 0.0:
        normal: Vec3 = Vec3.unit_vector(ray.at(t) - Vec3(0.0, 0.0, -1.0))
        return 0.5 * Vec3(normal.x() + 1, normal.y() + 1, normal.z() + 1)
    unit_direction: Vec3 = Vec3.unit_vector(ray.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)
