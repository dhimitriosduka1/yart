from tqdm import tqdm

from src.camera import Camera
from src.hittable.hittable_list import HittableList
from src.hittable.sphere import Sphere
from src.utils import write_ppm, ray_color, random_float
from src.vec3 import Vec3

if __name__ == '__main__':

    ASPECT_RATIO = 16.0 / 9.0
    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = int(IMAGE_WIDTH / ASPECT_RATIO)
    SAMPLES_PER_PIXEL = 100

    camera: Camera = Camera()

    hittable_list: HittableList = HittableList()
    hittable_list.add(Sphere(Vec3(0.0, 0.0, -1.0), 0.5))
    hittable_list.add(Sphere(Vec3(0.0, -100.5, -1.0), 100))

    data = []

    for j in tqdm(range(IMAGE_HEIGHT - 1, 0, -1)):
        for i in range(IMAGE_WIDTH):
            pixel_color = Vec3()
            for _ in range(SAMPLES_PER_PIXEL):
                u = float(i + random_float()) / (IMAGE_WIDTH - 1)
                v = float(j + random_float()) / (IMAGE_HEIGHT - 1)
                ray = camera.get_ray(u, v)
                pixel_color += ray_color(ray, hittable_list)
            data.append(pixel_color)

    write_ppm(data, IMAGE_WIDTH, IMAGE_HEIGHT, "../output/output.ppm", SAMPLES_PER_PIXEL)
