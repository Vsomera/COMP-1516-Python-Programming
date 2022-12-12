import random

"""
A module of functions
author: Vilmor
"""

def welcome_message():
    """
    A function that prints a welcome message
    First Varient: no param, no return
    :return: None
    """
    print("Welcome to COMP1516")

def welcome_message2(name):
    """
    A function that prints a welcome message with a name
    First Varient: 1 param, no return
    """
    print("Hello", name)

def get_random_num():
    """
    A function to return a random number
    No param, has return
    :return: a random number from 0.0 to 1.0
    """

    return random.random()

def calculate_area_square(side_length_n):
    """
    Function to calculate the area of a square
    has parameters, has return
    """

    return side_length_n ** 2

def get_product_description():
    return input("Please describe your product: ")

def get_amount():
    return input("how many of the item did you buy: ")

def get_price():
    return float(input("How much per item: "))

def calc_total():
    return


