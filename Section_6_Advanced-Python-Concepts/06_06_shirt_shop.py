# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# Cartesian product AxB of the sets A= {x,y,z} and B = {1,2,3}
cs = []

# for color in colors:
#     c += [(color, sizes[0]), (color, sizes[1]), (color, sizes[2])]
# for color in colors:
#     c = color
#     for size in sizes:
#         s = size
#         cs += (color, size)
    
# print(cs)

# cs = [(color, sizes[0:3:1]) for color in colors]
# cs = [s = size, cs += (color, size) for size in sizes, c = color for color in colors]
# print(cs)
cs = [[(color, size) for size in sizes]for color in colors]
print(cs)
# -or-
print([[(color, size) for size in sizes]for color in colors])

# -or-?

# inventory = set()
# ([inventory.add(color, size) for size in sizes]for color in colors)
# print(inventory)