# Using the given variables `base` and `digits`, write a dictionary comprehension
# that maps each integer between `0` and `999` to the list of three digits 
# that represents that integer in base 10. That is, the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
# 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
# 999: [9, 9, 9]}
#
# Your expression should work for any base. For example, 
# if you instead assign 2 to base and assign {0,1} to digits, 
# the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],
# ..., 7: [1, 1, 1]}

# webster = {}
# base = 10
# digits = set(range(base))
# key = 0

# if key in range(1000):
#     for a in digits:
#         for b in digits:
#             for c in digits: 
#                 value = tuple(f"{a}{b}{c}")
#                 webster.update({key:value})
#                 key += 1
# print(webster)
# it works!!
# now for comprehension...
# dictionary comprehension example:
# dict_1 = {"a": 1, "b": 2}
# dict_2 = {k: v*2 for (k, v) in dict_1.items()}
# another example:
# >>> d = {n: n**2 for n in range(5)}
# >>> print d
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# THE REAL DEAL!!!

base = 10
digits = set(range(base))

print({[list(f"{c}{b}{a}") for c in digits for b in digits for a in digits].index(n): n for n in [list(f"{c}{b}{a}") for c in digits for b in digits for a in digits]})

# -or the better one-
list_comp = [list(f"{c}{b}{a}") for c in digits for b in digits for a in digits]
print({list_comp.index(n) : n for n in list_comp})

# Theory

# list_abc = ['a', 'b', 'c']
# list_klm = ['k', 'l', 'm']
# list_xyz = ['x', 'y', 'z']
# key = 0
# webster = {}

# for a in list_abc:
#     for k in list_klm:
#         for x in list_xyz: 
#             value = tuple(f"{x}{k}{a}")
#             webster.update({key:value})
#             key += 1
# print(webster)

# webster_comp ={}
# list_comp = [list(f"{c}{b}{a}") for c in digits for b in digits for a in digits]
# print('\nstart\n')
# # print(list_comp)
# print('\nend\n')

# print({enumerate(list_comp) : list_comp for k,v in webster_comp.items()})

# webster_comp = {enumerate(k, start=0) : [[[tuple(f"{a}{b}{c}") for c in digits] for b in digits] for a in digits] for (k,v) in webster_comp.items()}
# print(webster_comp)



