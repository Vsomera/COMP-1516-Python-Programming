# COMP 1516 - Lab 4
# Vilmor Somera
# 10/12/2022

"""
Module of Functions for lab4.py
"""

def generate_password(first_name, last_name, bcit_id):
    """
    Returns Default Login Password and Generates a Password
    """
    first_name = first_name.capitalize()     # formats Variables
    last_name = last_name.capitalize()

    if len(first_name) >= 3:                 # Gets the first three letters from a properly-formatted first name; 
        first_name = first_name[0:3]         # if the first name length is less than three characters then the entire name will be used.
    else:
        first_name 

    if len(last_name) >= 3:                  # Gets the first three letters from a properly-formatted first name; 
        last_name = last_name[0:3]           # if the first name length is less than three characters then the entire name will be used.
    else:
        last_name

    if len(bcit_id) >= 3:                    # Gets the last three letters from the id
        bcit_id = bcit_id[-3]
    else:
        bcit_id

    return(f"{first_name}{last_name}{bcit_id}")

def cont_special(var_str):
    """
    Function returns true if there are no special characters in a given string
    """
    var_str.split()
    c=0
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    for i in range(len(var_str)):
        if var_str[i] in special_char:
            c+=1

    if c:
        return False                # string not accepted
    else:
        return True                 # string is accepted

def contains_num(var_str):
    """
    Function returns true if there is a single number in a given string
    """
    return any(char.isdigit() for char in var_str)


def contains_upper(var_str):
    """
    Function returns true if there is a single uppercase character in a given string
    """
    return any(char.isupper() for char in var_str)

def cont_lower(var_str):
    """
    Function returns true if there is a single lowercase character in a given string
    """
    return any(char.islower() for char in var_str)

def change_password():
    """
    Function will repedetly loop and prompt the user to enter a valid password.
    If the password meets the specifications, the loop will stopand return the user defined password
    """
    password = ""
    while password == "":
        password = input("Please Enter a Password: ")
        if (len(password) >= 7 and contains_num(password) and contains_upper(password) and cont_lower(password) and cont_special(password)) == True:
            print("***")
            print("Your password is:", password)
            print("***")
            return password
        else:
            password = ""
            print("---")
            print("Invalid Password, Please retype your password")
            print("---")
