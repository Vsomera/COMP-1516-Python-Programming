# COMP 1516 - Assignment 1
# Vilmor Somera
# 10/25/22

import data

def main():
    print("I should not be called")


def print_json_countries_and_capitals(): 
    """
    Function returns countries and captials and prints in JSON format using a while loop
    """
    x = len(data.countries_and_capitals)
    y = 0

    print("[")
    while y < x:
        country = data.countries_and_capitals[y][0]
        capital = data.countries_and_capitals[y][1]
        print("       {")
        print(f'             "country_name":"{country}",')
        print(f'             "capital_city":"{capital}"')
        print("       },")
        y += 1
    print("]")


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    Function returns list whose nth letters matches the letter in the parameter
    """ 
    list_of_countries = []
    x = n-1
    for char in data.countries:
        if char[x] == letter.lower():
            list_of_countries.append(char)

    return print(list_of_countries)


def get_doubled_letter_countries(): 
    """
    Function retursn a tuple of all the countries that have consecutive repeated letters
    """
    consec_vals = ["aa", "bb", "cc", "ee",
                    "ff", "gg", "hh", "ii",
                   "jj", "kk", "ll", "mm",
                    "nn", "oo", "pp", "qq",
                    "rr", "ss", "tt", "uu",
                    "vv", "ww", "xx", "yy",
                    "zz"]
    consec_countries = []
    for val in consec_vals:
        for country in data.countries:
            if val in country:
                consec_countries.append(country.lower())
    
    return print(tuple(i for i in consec_countries))
    # return print(consec_countries)

def get_funny_case_capital_cities(letter):
    """
    Function will take a letter param, and capitalize the letter around it
    """
    capital_list = []
    for capital in data.capitals:
        if letter in capital:
            capital = capital.lower()
            cap_len = len(capital) 
            idx = capital.rfind(letter) 
            capital = list(capital)

            if idx-1 < cap_len:
                capital[idx-1] = capital[idx-1].upper()
            
            if idx+1 < cap_len:
                capital[idx+1] = capital[idx+1].upper()

            capital = "".join(capital)
            capital_list.append(capital)

    return print(capital_list)
