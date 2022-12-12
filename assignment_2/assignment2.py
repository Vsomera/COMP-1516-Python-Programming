# COMP 1516 - Assignment 2
# Vilmor Somera
# 11/24/22

import data as d
import re


def write_countries_capitals_to_file(filename):
    """
    Function takes a file param and checks if the given param is a valid filename,
    it then writes the contents of capitals and countries to the file.
    """
    loop = True
    while loop == True:
        if 1 <= len(filename) <= 8:
            if (re.search(r'^[a-zA-Z0-9_]+\.txt$', filename)):
                with open(filename, 'w') as file:
                    for item in d.countries_and_capitals:
                        file.write(f'The capital of {item[0]} is {item[1]}\n')
                    loop = False
            else:
                filename = input("Please enter a valid text filename: ")
        else:
            filename = input("Please enter a valid text filename: ")


def save_capitals():
    """
    Function creates files containing capitals that fill a certain criteria using regex
    """
    # Creates a file with capitals that contain 3 consecutive vowels
    with open('vowel_vowel_vowel.txt', 'w') as file:
        vowels = r"[aeiou]{3,}"
        for capital in d.capitals:
            if re.findall(vowels, capital.lower()):
                file.write(f'{capital.lower()}\n')

    # Creates a file with capitals that contain 3 consecutive constants
    with open('cons_cons_cons.txt', 'w') as file:
        cons = r"[bcdfghjklmnpqrstvwxyz]{3,}"
        for capital in d.capitals:
            if re.findall(cons, capital.lower()):
                file.write(f'{capital.lower()}\n')
    
    # Creates a file with capitals that containa i somewhere before an e
    with open('i_before_e.txt', 'w') as file:
        for capital in d.capitals:
            if re.search('i', capital) and re.search('e', capital):
                if capital.rfind('i') < capital.rfind('e'):
                    file.write(f'{capital.lower()}\n')

    # Creates a file with capitals that starts with an a, and ends with a
    with open('a_a.txt', 'w') as file:
        for capital in d.capitals:
            if re.search('^A.*a$', capital):
                file.write(f'{capital.lower()}\n')

    # Creates a file with capitals that end with a vowel
    with open('end_with_vowel.txt', 'w') as file:
        for capital in d.capitals:
            if re.search('[aeiou]$', capital):
                file.write(f'{capital.lower()}\n')

    # Creates a file with capitals that contain an apostrophe, space, or x
    with open('wierd.txt', 'w') as file:
        for capital in d.capitals:
            if re.search("[' x]", capital):
                file.write(f"{capital.lower()}\n")

    # Creates a file with capitals that does not start with a-e, l-p, or s
    with open('not_start.txt', 'w') as file:
        for capital in d.capitals:
            capital = capital.lower()
            if not re.search("/^[a-e][l-p][s]/", capital):
                file.write(f"{capital}\n")
