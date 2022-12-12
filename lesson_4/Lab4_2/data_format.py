# COMP 1516 - Lab 4 Part 2
# Vilmor Somera
# 10/13/2022

"""
Module of Functions for main.py
"""

def get_book_info():
    """
    Function will ask for and remove trailing spaces from variables
    """
    book_title = input("Please enter book Title: ")
    book_isbn = input("Please enter book ISBN: ")
    book_author_last = input("Please enter book author Last Name: ")
    book_yr_pub = input("Please enter Year Publisher: ")
    book_price_usd = float(input("Please enter book price in USD: "))

    # Removes spaces at Beginning and at the end of the string 
    book_title = book_title.strip()
    book_isbn = book_isbn.strip()
    book_author_last = book_author_last.strip()
    book_yr_pub = book_yr_pub.strip()
    book_price_usd = '{0:.2f}'.format(book_price_usd)

    info = f"{book_title}//{book_isbn}//{book_author_last}//{book_yr_pub}//{book_price_usd}"
    return info

def csv_fomrat(var_str):
    """
    Function will return CSV format of a given string
    """
    var_str = var_str.replace("//","," )

    return var_str

def json_format(var_str):
    """
    Function will return JSON format of a given string
    """
    x = var_str.split("//")
    json_str = f'"title":"{x[0]}","isbn":"{x[1]}","author_last_name":"{x[2]}","year_published":"{x[3]}","price":"{x[4]}"'

    return json_str
