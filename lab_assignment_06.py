print("Author: Cantrell Picou Jr.")

print("Excersise 1")

#Import turtle
import turtle

#Length of side 
length = 5

#Draw square
for square in range(25):
    turtle.setheading(180)
    length += 5
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)

turtle.done()

print("Excersise 2")
#Import turtle
import turtle

#Starting position
forward = 50
left = 90

#Create picture
for side in range(25):
    turtle.left(left)
    turtle.forward(forward)
    forward = forward + 10
turtle.done()


print("Excersise 3")

def calculator():
    #Get input for loan, insurance, oil, tires, and maintenance
    loan = int(input("What is your loan payment: "))
    insurance = int(input("What is your imnsurance payment: "))
    oil = int(input("What is your oilpayment: "))
    tires = int(input("What is your tire payment: "))
    maintenance = int(input("What is your maintenance payment: "))

    #Calculate total 
    total = loan + insurance + oil + tires + maintenance

    #Display total 
    print("Your total monthly cost is ", total, sep=("$"))

calculator()


print("Excersise 4")
#Function 
def nutrition():
    #Get input for fat and carbs
    fat_grams = float(input("Number of fat grams consumed today: "))
    carb_grams = float(input("Number of carb grams consumed today: "))

    #Calculate to calories
    calories_from_fat = fat_grams * 9
    calories_from_carbs = carb_grams * 4

    #print out calculations
    print("Your total calories from fats are", format(calories_from_fat, ".0f"), "calories.")
    print("Your total calories from carbs are", format(calories_from_carbs, ".0f"), "calories.")

nutrition()
