# COMP 1516 - Lab 2
# Vilmor Somera
# 9/22/22
"""
Module of functions for main.py
"""
import math

def calculate_circle_area(radius):
    """
    Function takes radius as a param 
    and calculates and returns the area of the circle
    """
    return math.pi * radius**2

def calc_sphere_volume(radius):
    """
    Function takes radius as a param
    and calculates and returns the sphere volume
    """
    volume = (4/3)*math.pi*radius**3
    return volume

def calculate_BMI():
    """
    Function prompts user to enter the weight in kg, and heitght in meteres
    calculates and returns the body mass index
    """
    weight = float(input("Please enter weight in kg: "))
    height = float(input("Please enter height in meters: "))
    bmi = weight/(height*height)
    return bmi

def calc_hypotenuse():
    """
    Functiion prompts user to enter lengths of side A and side B of a right triange
    Function will then calculate and return the length of a right triangles hypotenuse
    """
    side_a = int(input("Please enter length of side A: "))
    side_b = int(input("Please enter length of side B: "))

    return float(math.hypot(side_a, side_b))
