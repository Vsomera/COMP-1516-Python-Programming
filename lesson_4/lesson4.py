# COMP 1516 - Lesson 4
# Vilmor Somera
# 10/11/2022


#print("hello world")
#a_string = "hello world"
#print(a_string)


""" Json and CSV Formats """

print("Hello\nThere")

def create_csv_example():
    """
    Function is an example of CSV format
    """
    first_name = "Bob"
    last_name = "Smith"
    years_employed = 10
    hourly_rate = 0 # because bob is a nigger

    # first way
    first_csv = first_name + ','+last_name+','+str(years_employed)+','+str(hourly_rate)
    # second way
    second_csv = "nigger"


""" Indexing and Slicing """

my_string = "Roses are red"
ch = my_string[7]
ch2 = my_string[6:9]
print(ch) # r
print(ch2) # are

# String Slicing
message = "Roses are red"
print(message[4:9])

def process_a_string(name):
    index = 0
    while index < len(name):
        print(name[index])
        index += 1
        
def has_upper(word):
    index = 0
    