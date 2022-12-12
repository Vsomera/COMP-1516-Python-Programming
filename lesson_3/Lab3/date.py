# COMP 1516 - Lab 3
# Vilmor Somera
# 10/09/22
"""
Script of functions for main.py
"""

def get_day_of_the_week(month, day, year):
    """
    Function will return the name of the day of the week for that month, day, and year
    """
    last_two_ofyr = year % 100
    step_one = last_two_ofyr // 12          
    step_two = last_two_ofyr - (step_one * 12)
    step_three = step_two // 4  

    if month == 4 or month == 7:
        total = step_one + step_two + step_three + day + 0
    if month == 1:
        if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:    
            total = step_one + step_two + step_three + day + 6
        else:
            total = step_one + step_two + step_three + day + 1

    if month == 10:
        total = step_one + step_two + step_three + day + 1
    if month == 5:
        total = step_one + step_two + step_three + day + 2
    if month == 8:
        total = step_one + step_two + step_three + day + 3
    if month == 3 or month == 11:
        total = step_one + step_two + step_three + day + 4
    if month == 2:
        if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:     
            total = step_one + step_two + step_three + day + 6
        else:
            total = step_one + step_two + step_three + day + 4
            
    if month == 6:
        total = step_one + step_two + step_three + day + 5
    if month == 9 or month == 12:
        total = step_one + step_two + step_three + day + 6

# Century Offsets
    if 1600 <= year <= 1699:     
        result = (total + 6) % 7
    if 1700 <= year <= 1799:
        result = (total + 4) % 7
    if 1800 <= year <= 1899:
        result = (total + 2) % 7
    if 1900 <= year <= 1999:
        result = total % 7
    if 2000 <= year <= 2099:
        result = (total + 6) % 7
    if 2100 <= year <= 2199:
        result = (total + 4) % 7

# Day of the Week
    if result == 0:     
        return "Saturday"
    elif result == 1:
        return "Sunday"
    elif result == 2:
        return "Monday"
    elif result == 3:
        return "Tuesday"
    elif result == 4:
        return "Wednesday"
    elif result == 5:
        return "Thursday"
    elif result == 6:
        return "Friday"


def is_leap_year(year):
    """
    Function will determine if the year parameter is a leap year
    """
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else:
        return False
