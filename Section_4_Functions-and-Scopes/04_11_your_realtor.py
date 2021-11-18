# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.
def realtor(**kwargs):
    kv_string = ''
    for k, v in kwargs.items():
        k_string = ''
        v_string = ''
        for i in k:    
            if i == '_':
                k_string += ' '
            else:
                k_string += i
        k = k_string.capitalize()
        if k == 'Price':
            v = "{:,}".format(v)
            v = f"${v}"
        else:
            pass
        kv_string += f"\n{k} = {v}"
    result = f"\nYour New House??\n{kv_string}\n"
    return print(result)   


# info to collect:
# square footage, price, location rating, bedrooms, baths, acreage, built, 
# ex_realty_dict = {'bedrooms': 3, 'bath': 2, 'price': 250000, 'location rating': 7.5, 'built': 1912, 'acreage':.33, 'square footage':2000}

realtor(bedrooms = 3, bath = 2, price = 250000, location_rating = 7.5, built = 1912, acreage = .33, square_footage = 2000)
