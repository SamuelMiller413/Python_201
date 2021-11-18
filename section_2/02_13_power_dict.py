# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
d = {}

for num in number_set:
    key = int(num)
    d[key] = (key * key)
print(d) 