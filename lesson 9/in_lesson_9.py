import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

# for file in BASE_DIR.glob("*"):
#     print(file)

filepath1 = BASE_DIR / "text.txt"

# file = open(filepath)
#
# data = file.read()
#
# print(data)
#
# file.close()

with open(filepath1, mode="a+") as file:
    # file.write("\nHelloooooooooooooo")
    file.seek(0)
    data = file.read()
    print(data)

filepath2 = BASE_DIR / "cat.jpg"

with open(filepath2, "rb") as file:
    print(file.read())

some_data = b"\x55\42\x0a"
print(some_data.hex())
