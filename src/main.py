# This is a sample Python script.
from src.utils import write_ppm


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    columns = 256
    rows = 256

    data = []

    for i in range(rows - 1, 0, -1):
        for j in range(columns):
            r = j / (columns - 1)
            g = i / (rows - 1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            data.append([ir, ig, ib])

    write_ppm(data, rows, columns, "output.ppm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
