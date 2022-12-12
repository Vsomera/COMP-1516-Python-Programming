# COMP 1516 - Lesson 9
# Vilmor Somera
# 11/23/22

import re

def is_valid_license_plate(car_license):
    """
    Function checks if the given string is a valid drivers liscense (eg. ABC123 or ABC 123)
    """
    if re.search("^[A-Z]{3}\\d{3}$|^\\d{3}[A-Z]{3}$|^[A-Z]{2}\\d ?\\d{2}[A-Z]$|^[A-Z]{2}\\d-\\d{2}[A-Z]$", car_license):
        return True
    else:
        return False

def is_valid_python_variable_name(var):
    """
    Between one and 32 char total: all char must be lowercase or underscores, but not more than one underscore in a row
    """
    if re.search("^[a-z_]{1,32}$", var):
            if not re.search("__", var):
                return True
            else:
                return False
    else:
        return False

def is_valid_email_address(email):
    """
    Function checks if the given email is a valid email address
    """
    if re.search("^[a-zA-Z_]{1,256}@[a-zA-Z_]{1,32}\.[a-zA-Z]{2,5}$", email):
        email_data = re.split("@", email)
        username = email_data[0]
        if not (username[0] == "_" or username[-1] == "_"):
            return True
        else:
            return False
    else:
        return False

def is_valid_human_height(height):
    """
    Function checks if the given height is a valid human height
    """
    height_array = re.split("'", height)
    feet = height_array[0]
    inches = height_array[1]

    if re.search("[2-8]", feet):
        if (inches[-1] == '\"') or (re.search("[in]$", inches)):
            if inches[-1] == '\"':
                inches_quote_removed = inches[:-1]
                print(int(inches_quote_removed))
                if re.search("^[0-9]$|^0[0-9]$|^1[01]$", inches_quote_removed):
                    if re.search("^[2]\'[0]\"$|^[2]\'[0]{2}\"$", height):
                        return False
                    else:
                        return True
                else:
                    return False
            elif re.search("[in]$", inches):
                inches_quote_removed = inches[:-2]
                if re.search("^[0-9]$|^0[0-9]$|^1[01]$", inches_quote_removed):
                    if re.search("^[2]\'[0]in$|^[2]\'[0]{2}in$", height):
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def main():
    print(is_valid_license_plate("ABC123"))
    print(is_valid_python_variable_name("first_name"))
    print(is_valid_email_address("Jason_Harrison@bcit.ca"))
    print(is_valid_human_height("2'1"))

if __name__ == "__main__":
    main()