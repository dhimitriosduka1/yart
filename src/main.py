from src.utils import write_ppm
from tqdm import tqdm

if __name__ == '__main__':
    columns = 256
    rows = 256

    data = []

    for i in tqdm(range(rows - 1, 0, -1)):
        for j in range(columns):
            r = j / (columns - 1)
            g = i / (rows - 1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            data.append([ir, ig, ib])

    write_ppm(data, rows, columns, "output.ppm")
