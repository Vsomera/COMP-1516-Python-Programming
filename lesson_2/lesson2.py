# COMP 1516 - Lesson 2
# Vilmor Somera
# 9/20/2022

# Example Function 1
def say_hello():
    print("hello")
    print("hello how are you")

say_hello() # calls function


# Example Function 2

name = input("Please enter your name: ")

def say_hello2(name):
    print("hello", name)
    print("hello how are you", name)

say_hello2(name) # calls function with parameter


# Example Function 3

def double_number(x):
    return 2 * x

result = double_number(15) # calls function

print(result)            
print(double_number(22)) # calls function with parameter 22

# Example Function 4

def triple(num):
    """ Takes in a number and returns its triple param num, 
    the number to be tripled returned is the tripled version
    """
    return 3 * num

print(triple(5)) # calls the function with the parameter 5

# Example Function 5

def pass_func():
    pass         # ignores the function

pass_func()      # calls the function


# Example Function 6 (Modules)

