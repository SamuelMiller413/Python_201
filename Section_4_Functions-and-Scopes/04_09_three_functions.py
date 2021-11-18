# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

import random

ex_list = [13, 23, 42, 69]
myst_list = []


def avg(list_):
    return sum_(list_)/len(list_)
    

def sum_(list_):
    return sum(list_)

def mystery(list_):
    def mystery(myst):
        top_shelf = (sum(myst)/len(myst)) / (sum(myst)/len(myst))
        top_shelf = top_shelf * 420
        return int(top_shelf)
    for num in list_:
        myst_list.append(num + 1)
        return mystery(myst_list)
    
def best(list_):
    list_dict = {}
    count = 0 
    def pick(dict_):
        x = random.randint(1,len(dict_))
        return dict_[x]
    for num in list_:
        list_dict.update({num:[count]})
        count += 1
    return pick(list_)
    

    


print(f"\nResults:\n        Average = {avg(ex_list)}\nBest number = {best(ex_list)}\nMystery Number = {mystery(ex_list)}")