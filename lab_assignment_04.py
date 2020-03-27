#Author: Cantrell Picou Jr.
print("Author: Cantrell Picou Jr.")

#Excersise 1
print("Excersise 1")

#Amount for rising level
rising = 1.6

print("Year", "\t", "Level")
# for loop to figure out what the increases is over the year
for num in range(26):
    level = rising * num
    print(num, "\t", format(level, ".1f"))

#Excersise 2
print("Excersise 2")


#Tuitiom increase
percent = .03
#Formula to calculate increase  
tuition = 8000.0

print("Year", "\t", "Tuition")
#for loop to display increase over the years
for num in range(6):
    tuition = (tuition * percent) + tuition
    print(num, "\t", format(tuition, ".2f"))

#Excersise 3
print("Excersise 3")

#input for number
user_input = int(input("Enter a number: "))
total = 1

#for loop to calculate 
for num in range(1, user_input + 1):
    total = total * num
print("The factorial of ", user_input, " is ", total, ".", sep=(""))

#Excersise 4
print("Excersise 4")

#import random number 
import random

#get random number 
random = random.randint(0, 101)

#user guess
user_guess = int(input("Enter a number: "))

#while loop to guess number 
while user_guess != random:
    if user_guess > random:
        print("Your number is to high, try again.")
        user_guess = int(input("Enter a number: "))
    elif user_guess < random:
        print("Your number is to low, try again.")
        user_guess = int(input("Enter a number: "))
print("You are correct, the number is", random)