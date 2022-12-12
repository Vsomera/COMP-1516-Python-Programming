# COMP 1516 - Lab 4
# Vilmor Somera
# 10/12/22

import login

def main():
    var1 = input("Please enter your First Name: ")
    var2 = input("Please enter your Last Name: ")
    var3 = input("Please enter your BCIT ID: ")
    print(login.generate_password(var1, var2, var3))
    login.change_password()
    
if __name__ == "__main__":
    main()
