# COMP 1516 - Lab 6
# Vilmor Somera
# 10/31/22

"""
Module of Functions for main.py
"""
import math

def get_square_numbers_between(first, last):
    """
    Function creates and returns a list of all the square numbers between (and including) first and last.
    """
    sqr_nums = []
    for num in range(first, last):
        root_num = math.sqrt(num)
        if int(root_num + 0.5) ** 2 == num:
            sqr_nums.append(num)

    return print(sqr_nums)


def process_user_input():
    """
    Function repeatedly asks the user to enter numbers, or type 0 to quit entering numbers
    """
    num_list = []

    loop = 1
    while loop == 1:
        usr_input = int(input("Enter a number or 0 to end: "))
        if usr_input == 0:
            loop = 0
        else:
            num_list.append(usr_input)
    
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num

    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num

    sum = 0
    for num in num_list:
        sum += num
    
    print("Your numbers are: ", num_list)
    print("Sum is: ", sum)
    print("Min is: ", min)
    print("Max is: ", max)
