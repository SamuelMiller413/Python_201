
from pathlib import Path

starting_path = "/Users/admin/CodingNomads/Python 201/03_file-input-output"
current_path = Path.cwd()


# Absolute path:

# with open("/Users/admin/Desktop/input.txt", "r") as file_in:
#     print(file_in.read())


# Using pathlib module for 'operating-system agnostic' path

# data_path = Path("/users/admin/Desktop")
# with open(data_path.joinpath("input.txt"), "r") as file_in:
#     print(file_in.read())

# filepath = Path("/Users/admin/Desktop/input.txt")

# with filepath.open() as f:
#     print(f.read())

p = Path("hello.txt")
p.write_text("Hello world!")
p.read_text()
test = p.read_text()
print(test)
