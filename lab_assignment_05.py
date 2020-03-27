
print("Author: Cantrell Picou Jr")

print("Excersise 1")

#total
total = 1 
#input for number
user_input = int(input("Enter a number between 2 and 20: ")) 

#validation for number 

#calulate factorial number
while user_input != 0:
    while user_input < 0 or user_input > 20:
        if user_input < 0:
            user_input = int(input("Enter a positive number between 2 and 20: "))
        elif user_input > 20:
            user_input = int(input("Enter a positive number between 2 and 20: "))
        else:
            break

    for num in range(1, user_input + 1):
        total *= num
    print(total)
    user_input = int(input("Type a number between 2 and 20 or 0 to stop: "))


print("Excersise 2")

#calculate triangle
for row in range(6, -1, -1):
    for col in range(row + 1):
        print("*", end=(""))
    print("")


print("Excersise 3")

#total
counter = 30
total_2 = 0


#calulate total
while counter > 0:
    for i in range(1, 31):
        total_2 = total_2 + (i / counter)
        if i == 30 and counter == 1:
            print("(", i, "/", counter, ")", " =", sep=(""))
        else:
            print("(", i, "/", counter, ")", " +", sep=(""))
        counter -= 1
print("The total is", format(total_2, ".2f"))



print("Excersise 4")

import random

random_num = random.randint(0,1)


#output for heads/tails
for num in range(21):
    random_num = random.randint(0,1)
    if random_num == 1:
        print("Tails")
    else:
        print("Heads")


