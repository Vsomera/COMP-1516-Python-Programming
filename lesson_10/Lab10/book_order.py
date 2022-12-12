# COMP 1516 - Lab 10
# Vilmor Somera
# 12/06/2022

import sys
import re
import os
from book_order_utils import validate_book_order_details, calculate_per_book_cost, write_book_order_details


def main():
    print(sys.argv)
    length_argument = len(sys.argv)
    print(length_argument)
    print()
    if length_argument == 8:
        print("validate_book_order_details")
        validate_book_order_details(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        print()
        print("calculate_per_book_cost")
        print(calculate_per_book_cost(float(sys.argv[7]), float(sys.argv[6])))
        print()
        print("write_book_order_details")
        filename = input("Please enter a file name: ")
        unit_cost = input("Please enter a unit cost: ")
        write_book_order_details(filename, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], unit_cost)
    else:
        print("Make sure you only have 7 command line arguments")


if __name__ == '__main__':
    main()