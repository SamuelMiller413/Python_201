


locations = ['indonesia', 'spain', 'thailand', 'mexico', 'usa']
# for index, country in enumerate(locations, start = 1):
#     print(f"* {index}: {country}")



def my_enumerate(input, start=0):
    output = ()
    for item in input:
        output +=(start, item) 
        start += 1
    return output

print(my_enumerate(locations))

for index, country in enumerate(locations, start = 10):
    print(f"* {index}: {country}")