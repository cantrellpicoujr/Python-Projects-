#Author: Cantrell Picou Jr.
print("Author: Cantrell Picou Jr.")
print("**********Excersise 1***********")

#input for data
r = float(input("Enter the length of the row, in feet: "))
e = float(input("Enter the amount of space used by an end-post assembly, in feet: "))
s = float(input("Enter the amount of space between the vines, in feet: "))

#Formula to calculate the number of grapevines that will fit in a row
v = (r - 2) * e / s 

#print function to display number
print("The number of grapevines that will in the row is:", format(v, ".0f"))


print("**********Excersise 2***********")

#Input for age
age = int(input("Enter your age: "))

#If/else statement for to print out life stage
if age <= 1:
    print("You are an infant.")
elif age > 1 and age <= 13:
    print("You are an child.")
elif age > 13 and age <= 20:
    print("You are an teenager.")
else:
    print("You are an adult.")

print("**********Excersise 3***********")

#Input function for mass
mass = float(input("What is the objects mass: "))

#Formula to calculate weight
weight = mass * 9.8

#If/else statement to display weight of object
if weight < 100:
    print("The object is to light.")
elif weight > 500:
    print("The object is to heavy.")

print("**********Excersise 4***********")
#Input for miles
miles = int(input("What is the distance in miles: "))
#Input for age
age = int(input("What is your age: "))
##Data for program
first_mile = 2.00
less = .25
more = .10
discount = .2

#If/else statement to determine miles traveled
if miles <= 10:
    sub_total = first_mile + (miles-1) * less
elif miles > 10:
    sub_total = (9 * less) + first_mile + (miles - 10) * more

#If/else statement to determine if a person qualifies for discount 
if age <= 18 or age >= 60:
    total = sub_total - (sub_total * discount) 
    print("Your total amount for this trip is", format(total, ".2f"))
else:
    total = sub_total
    print("Your total amount for this trip is", format(total, ".2f"))
 