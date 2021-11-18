# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
    >Converts km to miles.
    Args: km (int): the amount of km requiring conversion.
    Returns: miles (str): conversion into miles of given km input.
    """
    miles = km * 0.6
    return miles

km = int(12)
print(km_to_miles(km))

print(km_to_miles.__doc__)
