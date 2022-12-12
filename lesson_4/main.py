# Lesson 4
def formatting():
    name = "Bob"
    item = "apples"
    quantity = 10

    print(name, "bought", quantity, item, "from the store")
    # message = name, "bought", quantity, item, "from the store"
    # print(message)
    # print(type(message))
    message = "%s bought %.2f %s from the store"%(name, quantity, item)
    print(message)
    message = f"{name} bought {quantity:.2f} {item} from the store"
    print(message)
    message = "{} bought {:.2f} {} from the store".format(name, quantity, item)
    print(message)


def slicing():
    string = "apple#banana#cherry#orange"
    print(len(string))
    print(string[25])
    print(string[7])
    print(string[-1])
    print(string[6:12])
    print(string[6:45])
    print(string[6:])
    # print(string[45])
    print(string)
    var1 = string[6:12]
    print(var1)
    print(string)

    string_split = string.split('#')
    print(string_split)
    string_split = "/".join(string_split)
    print(string_split)
    string_dollar = string_split.replace("/", "$")
    print(string_split)
    print(string_dollar)


def string_functions():
    print("hello".islower())
    print("HELLO".isupper())
    print("hELLO".isupper())
    print("heLLo123".isalnum())
    print("heLLo".isalnum())
    print("hello123".isalnum())
    print('123'.isalnum())

    # password = "hello"
    # if password.isupper():
    #     print("You need at least a lower case letter")
    # if password.islower():
    #     print("You need at least one upper case letter")

    while True:
        password = input("Please enter your password")
        if has_upper(password):
            print("thanks for the uppercase letter, bye")
            break


def process_a_string(name):
    index = 0
    while index < len(name):
        print(name[index])
        index += 1


def has_upper(word):
    index = 0
    while index < len(word): # hellO
        # print(word[index])
        # index += 1
        if word[index].isupper():
            return True
        index += 1

    return False



def main():
    # formatting()
    slicing()
    # string_functions()
    # print(has_upper("hellaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaLLLaaaaaaaaaaadafdsaf"))
    # process_a_string("Hello Goodbye Aloha")
    # if "E".isupper():
    #     print('that E is uppercase')

if __name__ == '__main__':
    main()