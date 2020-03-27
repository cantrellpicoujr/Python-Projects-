print("Author: Cantrell Picou Jr")
#Author: Cantrell Picou Jr
"""
#Excersise 1
print("**********Excercise 1**********")

#Input for purchased packages
quantity = int(input("How many packages have you purchaed: "))

#Package value
package = 99.00

#If/else statement to qualify for discount
if quantity >= 10 and quantity <= 19:
    discount = .10
    total = (package * quantity) - (discount * package)
    print("Your discount is", format(discount, ".0%"))
    print("Your total is $", format(total, ".2f"), sep=(""))
elif quantity >= 20 and quantity <= 49:
    discount = .20
    total = (package * quantity) - (discount * package)
    print("Your discount is", format(discount, ".0%"))
    print("Your total is $", format(total, ".2f"), sep=(""))
elif quantity >= 50 and quantity <= 99:
    discount = .30
    total = (package * quantity) - (discount * package)
    print("Your discount is", format(discount, ".0%"))
    print("Your total is $", format(total, ".2f"), sep=(""))
elif quantity >= 100:
    discount = .40
    total = (package * quantity) - (discount * package)
    print("Your discount is", format(discount, ".0%"))
    print("Your total is $", format(total, ".2f"), sep=(""))
else:
    print("You get no discount.")


#Excersise 2
print("**********Excercise 2**********")

#Input for weight
weight = float(input("What is the weight of the package: "))

#If/else statement for weight cost 
if weight <= 2:
    total = weight * 1.50
    print("The shipping charge for your item is $", format(total, ".2f"), sep=(""))
elif weight > 2 and weight <= 6:
    total_2 = weight * 3.00
    print("The shipping charge for your item is $", format(total, ".2f"), sep=(""))
elif weight > 6 and weight <= 10:
    total = weight * 4.00
    print("The shipping charge for your item is $", format(total, ".2f"), sep=(""))
else: 
    total = weight * 4.75
    print("The shipping charge for your item is $", format(total, ".2f"), sep=(""))



#Excersise 3
print("**********Excercise 3**********")

#Input for diet restrictions
vegetarian = input("Is anyone in the group vegetarian? ")
vegan = input("Is anyone in the group vegan? ")
glutten = input("Is anyone in the group glutten-free? ")

#If/else statement for resturants
if vegetarian == "yes" and vegan == "yes" and glutten == "yes":
    print("Here are your resturant choices:\n", "Corner Cafe \n", "The Chefs Kitchen")
elif vegetarian == "yes" and vegan == "no" and glutten == "yes":
    print("Here are your resturant choices:\n", "Corner Cafe \n", "Main Street Pizza Company\n", "The Chefs Kitchen")



#Excersise 4
print("**********Excercise 4**********")

#Input for number
number = int(input("Type a number: (Type '-1' to stop) "))

#While loop for number 
while number > 0:
    if number == 1:
        print("How are you?")
        number = int(input("Type a number: (Type '-1' to stop) "))
    elif number == 2:
        print("Good Job!")
        number = int(input("Type a number: (Type '-1' to stop) "))
print("Goodbye and have a nice day!")


number = int(input(("Enter a number: ")))

while True:
    if number >= 0 and number <= 100: 
        print("Your number was", number)
        break
    else: 
        number = int(input(("Pick a number between 0 and 100: ")))
"""


