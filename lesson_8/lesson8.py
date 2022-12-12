# COMP 1516 - Lesson 8
# Vilmor Somera
# 11/14/22

"""
Basic File Opening syntax
"""
# with open('books.txt', 'r') as file:
#   for line in file:
#        print(line.strip()) stip removes \n from outputs
    # text = file.read()
    # text = file.readlines()
    # text = file.readline()
    # print(text)

    # print(repr(text)) # includes "/n" at the end of each line

"""
Opens File as a String
"""
a_list = []
with open('books.txt', 'r') as file:
    file_as_string = file.readlines()
    # print("entire file is %s" % file_as_string)
    print(file_as_string)
    for line in file_as_string:
        line = line.strip()
        a_list.append(line)
    print(a_list)
"""
Overwriting a File if the file already exists
"""
# with open('books.txt', 'w') as file:
#   file.write("Hello")

"""
Appending to a File
"""
# with open('books.txt', 'a') as file:
#    file.write("Hello Word\nGoodbye World")

