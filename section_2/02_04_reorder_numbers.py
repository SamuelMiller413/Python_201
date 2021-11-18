# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


list_10 = []
stri_10 = ""
count = 0
flag = True

while flag == True:
    answer = input("please enter a number between 1 and 100\n   > ")
    if answer.isdigit():
        answer = int(answer)
        if answer <= 100:
            list_10.append(answer)
            count += 1
            if count == 10:
                flag = False
        else:
            print("please follow the rules")
    else:
        print("please follow the rules")
# list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # for testing

for i in list_10:
    if i == list_10[-1]:
        stri_10 += str(i)
    else:
        stri_10 += str(i) + ", "

output = ""

stri_1 = list_10[1::2]
stri_2 = list_10[-2::-2]

for i in stri_1:
    output += str(i) + ", "
for i in stri_2:
    if i == list_10[0]:
        output += str(i)
    else:
        output += str(i) + ", "
print(f"Input: {stri_10}")
print(f"Output: {output}")