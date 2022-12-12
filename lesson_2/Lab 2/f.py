# COMP 1516 - Lab 2
# Vilmor Somera
# 9/22/22

""" 
Module of functions for retail_item.py
"""

def get_retail_item_desc():
    """
    Function returns item description from user input
    """
    return input("Please enter item description: ")

def get_num_of_purchased_items():
    """
    Function asks the user the quantity sold from the user adn returns the value
    """
    return int(input("Please enter quantity sold: "))

def get_price_usd_per_unit():
    """
    Function asks user to enter price in USD and returns it
    """
    return float(input("Please enter price in USD: ")) 

def get_tax_rate():
    """
    Function asks user to enter tax rate as a float value and returns it
    """
    return float(input("Please enter tax rate: "))

def calc_subtotal_usd(usd, q_sold):
    """
    Function takes 2 parameters: USD and quantity sold
    and calculates and returns the subtotal amount in USD 
    """
    return usd * q_sold

def calc_tax_usd(subtotal, tax):
    """
    Function takes 2 param: subtotal and tax
    and calculates and returns the tax amount of the given subtotal all in american dollars
    """
    return subtotal * tax

def calc_total_usd(subtotal, tax):
    """
    Function takes 2 param: subtotal and tax
    and calculates and returns the total amount including tax in USD
    """
    return subtotal + tax