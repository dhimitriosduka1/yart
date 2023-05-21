from tqdm import tqdm

from src.camera import Camera
from src.hittable.hittable_list import HittableList
from src.hittable.sphere import Sphere
from src.utils import write_ppm, ray_color
from src.vec3 import Vec3

if __name__ == '__main__':

    aspect_ration = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ration)

    camera: Camera = Camera()

    hittable_list: HittableList = HittableList()
    hittable_list.add(Sphere(Vec3(0.0, 0.0, -1.0), 0.5))
    hittable_list.add(Sphere(Vec3(0.0, -100.5, -1.0), 100))

    data = []

    for j in tqdm(range(image_height - 1, 0, -1)):
        for i in range(image_width):
            u = float(i) / (image_width - 1)
            v = float(j) / (image_height - 1)

            ray = camera.get_ray(u, v)
            color = ray_color(ray, hittable_list)

            data.append(color)

    write_ppm(data, image_width, image_height, "../output/output.ppm")
