from src.ray import Ray
from src.utils import write_ppm, write_color
from tqdm import tqdm

from src.vec3 import Vec3

if __name__ == '__main__':

    aspect_ration = 16.0 / 9.0
    rows = 400
    columns = int(rows / aspect_ration)

    viewport_height = 2.0
    viewport_width = viewport_height * aspect_ration
    focal_length = 1.0

    origin = Vec3(0.0, 0.0, 0.0)
    horizontal = Vec3(viewport_width, 0.0, 0.0)
    vertical = Vec3(0.0, viewport_height, 0.0)

    # This means that the z axis penetrates the viewport exactly in the middle
    lower_left_corner = origin - (horizontal / 2) - (vertical / 2) - Vec3(0.0, 0.0, focal_length)

    data = []

    for j in tqdm(range(columns - 1, 0, -1)):
        for i in range(rows):
            u = float(i) / (columns - 1)
            v = float(j) / (rows - 1)

            ray = Ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            color = ray.ray_color()

            data.append(color)

    write_ppm(data, rows, columns, "output.ppm")
