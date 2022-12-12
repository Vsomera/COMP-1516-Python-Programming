# COMP 1516 - Lesson 10
# Vilmor Somera


"""
TypeError vs ValueError
"""
# x = int("hello")
# this is a ValueError; the value “hello” cannot be converted to an int

# print("hello" + 123)
# this is a TypeError; the + sign joins int-to-int or str-to-str only


"""
Exception Handling: Syntax
"""

# try:
# ... Normal code that might produce exceptions
# except: # Go here is any exception occurs in the try block
# ... Exception handling code

"""
Exceptinon Handling: Multiple Syntax
"""
# try:
# # ... Normal code
# except exceptiontype1:
# # Code to handle exceptiontype1
# except exceptiontype2:
# # Code to handle exceptiontype2
# except:
# # Code to handle other exception types

# try:
# # ...
# except(ValueError, TypeError):
# # Exception handler for any ValueError or TypeError that occurs.
# except(NameError, AttributeError):
# # A different handler for NameError and AttributeError exceptions.
# except:
# # A different handler for any other exception type.

"""
Exception Handling: Example
"""
# try:
#     weight_kg = int(input("Enter weight in kg: "))
#     weight_lbs = float(weight_kg) / 0.454
#     print("Weight in pounds is %f" % weight_lbs)
# except:
#     print("Error: Could not calculate the weight in pounds")

"""
Raising Exceptions
"""
# try:
#     weight_kg = int(input("Enter your weight in kg: "))

#     if weight_kg > 1000:
#         raise ValueError("Weight is too big!")

#     weight_lbs = float(weight_kg) / 0.454

#     print("Weight in pounds is %f" % weight_lbs)

# except ValueError:
#     print("Error: Could not calculate the weight in pounds")


# try:
#     weight_kg = int(input("Enter weight in kg: "))

#     if weight_kg > 1000:
#         raise ValueError("Weight is too big!")
#     weight_lbs = float(weight_kg) / 0.454
#     print("Weight in pounds is %f" % weight_lbs)
# except ValueError as v:
#     print(str(v))   

"""
Exception Handling: Cleanup
"""
# try:
# # ... Normal code
# except:
# # ... Handle exception
# finally:
# # always executed; e.g. clean-up actions:


"""
Interacting with the Filesystem
"""
# use os.path.join() to create a portable file oath string
# os.path.join('subdir', 'mobile.jpg')

# os.path.split(path) – Splits a path into a 2-tuple (head, tail), where tail is the last token in the
# path string and head is everything else
# • os.path.exists(path) – Returns True if path exists, else returns False.
# • os.path.isfile(path) – Returns True if path is an existing file, and false otherwise (e.g., path is a
# directory).
# • os.path.getsize(path) – Returns the size in bytes of path.
# • os.walk() - 'walks' a directory tree like the one above, visiting each subdirectory in the specified
# path. The example on the next slide walks a user-specified path of the above directory tree.
