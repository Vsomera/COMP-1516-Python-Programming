# COMP 1516 - Lesson 5
# Vilmor Somera
# 10/18/22



""" Tuples """

def tuples_examples():
    car_makers = ("dodge", "ford", "honda", "toyota", "dodge")
    print(car_makers.count("dodge")) # 2; there are 2 instances of "dodge"
    print(car_makers.count("ford")) # 1
    print(car_makers.count("lamborghini")) # 0


""" Tuple: Multiple Return """

def get_name_from_user():
    first = input("What is your first name? ")
    middle = input("What is your middle name? ")
    last = input("What is your last name? ")
    
    return (first, middle, last) # a tuple; notice the parentheses; returns ONE tuple containing MANY elements

# full_name = get_name_from_user() # full_name is a tuple of three strings
# print("Your full name is %s %s %s" % (full_name[0], full_name[1], full_name[2]))


""" Letters and Functions and Methods """

def letters_functions_methods():
    letters = []
    letters = ["a", "b", "x", "y", "z"]
    letters.pop() # removes the last element: z; could also do letters.pop(0) which removes the first element (here, ‘a’), etc...
    letters.remove("y") # removes the first instance of y
    letters[2] = "c" # the third element (x) is updated to become c
    letters.append("d") # appended to the end of the list
    letters.append("e")
    letters.insert(0, 's')
    more_letters = ["f", "g", "h", "i", "j", "k"]
    all_letters = letters + more_letters # joins together (“concatenates”) multiple lists with the plus + sign

    return print(all_letters) # ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


""" Lists of Lists """

def lists_of_lists():
    row_0 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row_1 = ["i", "j", "k", "l", "m", "n", "o", "p"]
    row_2 = ["q", "r", "s", "t", "u", "v", "w", "x"]
    row_3 = ["y", "z"]
    
    table = [row_0, row_1, row_2, row_3]
    print(table)

    row = 0
    while row < len(table):
        print(table[row])
        col = 0
        while col < len(table[row]):
            print(table[row][col], end =' ')
            col += 1
        row += 1
        print()


letters_functions_methods()