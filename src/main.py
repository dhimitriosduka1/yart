from src.utils import write_ppm, write_color
from tqdm import tqdm

from src.vec3 import Vec3

if __name__ == '__main__':
    columns = 256
    rows = 256

    data = []

    for i in tqdm(range(rows - 1, 0, -1)):
        for j in range(columns):
            r = j / (columns - 1)
            g = i / (rows - 1)
            b = 0.25
            color = Vec3(r, g, b)
            data.append(color)

    write_ppm(data, rows, columns, "output.ppm")
