# COMP 1516 - Lesson 3
# Vilmor Somera
# 9/7/22

age_in_years = int(input("Please enter your age: "))

if age_in_years >= 16:
    print("you can drive")
else: 
    print("you cannot drive")

number = int(input("Please enter a number: "))

if number%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

grade = 75
print("Say for example you grade is", grade)

if grade >= 60:
    print("Your grade is D")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 90:
    print("Your grade is A")

x = True
y = True
z = True

print(x and y or z)
print(x and (y or z))

i = 2

while i <= 100:
    print(i)
    i += 2

while True:
    user_input = input("Please enter x to stop: ")
    if user_input.lower == "x":
        exit()

