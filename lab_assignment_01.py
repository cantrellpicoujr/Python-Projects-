#This is excercise 1
print("***********Exercise 1**************")
#User inputs for name, address, number, and major
name = input("What is your name\n")
address = input("What is your address?\n")
number = input("What is your phone number?\n")
major = input("What is you major?\n")
#Print function to print out these items
print("Name:", name, "Address:", address, "Number:", number, "Major:", major, sep=("\n"))

#This is excercise 2
print("***********Exercise 2**************")
#User input for projected sales
total = int(input("Enter the projected amount of total sales?\n"))
#Fourmula to calculate profit
total_sales = total * 0.23
#Print function to display profit
print("Your total profit is " + format(total_sales,".2f"))

#This is excercise 3
print("***********Exercise 3**************")
#Formulas to calculate distance 
distance_1 = 70 * 6
distance_2 = 70 * 10
distance_3 = 70 * 15
#Print function to display distance calculations
print(str(distance_1), str(distance_2), str(distance_3), sep="\n")

#This is excercise 4
print("***********Exercise 4**************")
#User inputs for miles driven and gallons used
driven = int(input("How many miles have you driven?\n"))
gallons_used = int(input("How many gallons of gas have you used?\n"))
#Formula to calculate miles per gallon
mpg = driven / gallons_used 
#Print function to dispay miles per gallon
print("The miles per gallon for your car is " + format(mpg, ".2f"))
