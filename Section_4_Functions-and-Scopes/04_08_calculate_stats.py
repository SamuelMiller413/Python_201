# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.


example_list = [1, 2, 3, 4, 5, 6, 7]
list_of_numbers = []
flag = True
max = None
min = None
avg = None
sum_ = None

def stats(list_):
  list_.sort()
  max = list_[-1]
  min = list_[0]
  avg = sum(list_)/len(list_)
  sum_ = sum(list_)
  return f"\nStats for given list:\n Max = {max}\n Min = {min}\n Average = {avg}\n Sum = {sum_}\n"

# call the function below here
# list_of_numbers = example_list

num = input(f"\nEnter a number to begin the list:\n   ")

if num.isdigit():
    num = int(num)
    list_of_numbers.append(num)
else:
    print("\n*Numbers only*\n")
    
while flag == True:
    num = input(f"\nEnter a number to continue the list:      (if done, type '=')\n ")
    if num == '=':
        flag = False
    else:
        if num.isdigit():
            num = int(num)
            list_of_numbers.append(num)
        else:
            print("\n*Numbers only*\n")
print(stats(list_of_numbers))
