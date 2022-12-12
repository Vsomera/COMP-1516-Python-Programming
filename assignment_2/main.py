# COMP 1516 - Assignment 2
# Vilmor Somera
# 11/24/22
    
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import assignment2 as a2

def main():
    a2.write_countries_capitals_to_file("0123456789.txt")
    a2.save_capitals()

if __name__ == "__main__":
    main()
