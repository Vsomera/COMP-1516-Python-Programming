# COMP 1516 - Lab 10
# Vilmor Somera
# 12/06/2022

import re
import os

def validate_book_order_details(order_num, title, author, 
                                isbn, year_pub, quantity, 
                                cost_cad):
    try:
        print("--Order Number-")
        order_num_converted = int(order_num)
        if type(order_num_converted) == int:
            order_num_array = [order_num]
            removed_leading_zeros = [ele.lstrip('0') for ele in order_num_array]
            leading_zeros_amount = 0
            while True:
                if len(removed_leading_zeros[0]) == leading_zeros_amount:
                    break
                else:
                    leading_zeros_amount += 1
            print(leading_zeros_amount)
            print("--Title--")
            if re.search("^[a-zA-Z\s]+$", title):
                print(title)
                print("--author--")
                if re.search("^[a-zA-Z\s\'\"]+$", author):
                    print(author)
                    print("--ISBN--")
                    if re.search("^[0-9]{4,20}$", isbn):
                        print(isbn)
                        print("--Year--")
                        if re.search("^[0-9]{4}$", year_pub):
                            print(year_pub)
                            print("--Quantity--")
                            if re.search("^([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|1000)$", quantity):
                                print(quantity)
                                print("--Cost--")
                                if re.search("^\d+\.\d{2}$", cost_cad):
                                    print(cost_cad)
                                    return True
                                else:
                                    raise ValueError("cost must be a floating point value with exactly 2 decimal places")
                            else:
                                if (len(quantity) <= 0 or len(quantity) >= 4) and type(quantity) != int:
                                    raise ValueError("quantity must be between 0 and 1000, inclusive")
                                raise TypeError("quantity must be an integer")
                        else:
                            if len(year_pub) > 4 or len(year_pub) < 4:
                                raise ValueError("year must be 4 digits exactly.")
                            raise TypeError("year must be a integer.")
                    else:
                        raise TypeError("ISBN must be an integer and between 4 and 20 digits, inclusive")
                else:
                    raise ValueError("Author is invalid")
            else:
                raise ValueError("There is no lower, uppercase letter(s) or spaces")
        else:
            raise ValueError('invalid order number')
    except ValueError as e:
        print("The ValueError is " + str(e))
    except TypeError as e:
        print("The TypeError is " + str(e))


def calculate_per_book_cost(cost_cad, quantity):
    """
        A function that will calculate the cost per book
        Second Variant, parameter, and return
        :param quantity: the quantity ordered in integer between 0 and 1000
        :param cost: The cost of the book in floating point with 2 decimal places
        :return: error or cost of book
    """
    try:
        cost_per_book = cost_cad / quantity
        return cost_per_book
    except ZeroDivisionError:
        return "The quantity cannot be zero. No Books in Order."


def write_book_order_details(filename, title, author, isbn, year_pub, quantity, cost_cad, unit_cost):
    """
        A function that will write the book order details in a file
        Third Variant, and parameter
        :param filename: the name of the file with <name>.txt
        :param title: the title of the book
        :param author: the author of the book
        :param isbn: the isbn of the book
        :param year: the year the book was published
        :param quantity: the quantity ordered in integer between 0 and 1000
        :param cost: The cost of the book in floating point with 2 decimal places
        :param unit_cost: The cost to produce the product
    """
    print(filename)
    path = 'C:/Users/monik/Desktop/new4/Lesson 10 Exceptions/Lab10/' + filename
    isExist = os.path.exists(path)
    print(isExist)
    if isExist == True:
        raise ValueError("Order file name  already exists!")
    file_script = open(filename, "w")
    print("--Validating--")
    validating = validate_book_order_details("1", title, author, isbn, year_pub, quantity, cost_cad)
    print(validating)
    while True:
        if validating:
            try:
                if re.search(r"^[a-zA-Z0-9]{1,}.txt$", filename):
                    file_script.write('BOOK ORDER\n' +
                                      'title=' + title + '\n' +
                                      'author=' + author + '\n' +
                                      'isbn=' + isbn + '\n' +
                                      'year=' + year_pub + '\n' +
                                      'quantity=' + quantity + '\n' +
                                      'cost=$' + cost_cad + '\n' +
                                      'unit_cost=$' + unit_cost
                                      )
                    file_script.close()
                    break
                else:
                    raise ValueError("the file name must only contains letters and/or numbers.")
            except FileExistsError:
                filename = input("Please enter another file name because it has already been used: ")
            except ValueError as e:
                print("The ValueError is " + str(e))
                break
            except TypeError as e:
                print("The TypeError is " + str(e))
                break
        else:
            print("You have values that are not correctly entered. Try running the code again")
            break