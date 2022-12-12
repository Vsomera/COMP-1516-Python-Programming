# COMP 1516 - Lab 2
# Vilmor Somera
# 9/22/22
import utilities

def main():
    radius_input = float(input("Please enter the radius of a circle in cm: "))
    print(utilities.calculate_circle_area(radius_input))
    
    sphere_input = float(input("Please enter the radius of a sphere in cm: "))
    print(utilities.calc_sphere_volume(sphere_input))

    print("the body Mass Index is", utilities.calculate_BMI())

    print("The hypotenuse length of the right trienagle is", utilities.calc_hypotenuse())
    

if __name__ == "__main__":
    main()
