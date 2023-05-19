def write_ppm(data, rows, cols, path):
    with open(path, "w") as image:
        image.write("P3\n")
        image.write(f"{cols} {rows}\n")
        image.write("255\n")

        for entry in data:
            image.write(f"{entry[0]} {entry[1]} {entry[2]}\n")
