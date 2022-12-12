# COMP 1516 - Lab 8
# Vilmor Somera
# 11/20/22

import data as d

def get_countries(substring):
    """
    Function loops through the countries tuple. If a country contains the substring param, 
    creates a brand-new file named "MatchingCountries.txt" for writing, and writes that country name on its own line in the file.
    """
    for country in d.countries:
        if substring in country:
            with open('MatchingCountries.txt', 'a') as file:
                file.write(f"{country}\n")


def get_capitals(substring):
    """
    Function re-opens the "MatchingCountries.txt" file for appending, loops through the capitals tuple.
    If a capital contains the substring, appends to the end of the file.
    """
    for capital in d.capitals:
        if substring in capital:
            with open('MatchingCountries.txt', 'a') as file:
                file.write(f"{capital}\n")

def print_file_data():
    """
    Function re-opens "MatchingCountries.txt" file for reading.
    Uses readlines function to loop throught the file and display each of the lines to the screen.
    """
    with open('MatchingCountries.txt', 'r') as file:
        f_contents = file.readlines()
        for line in f_contents:
            print(line.strip())


def main():
    get_countries("an")
    get_capitals("os")
    print_file_data()

if __name__ == "__main__":
    main()
    