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
