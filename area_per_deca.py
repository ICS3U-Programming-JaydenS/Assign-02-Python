#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 6, 2025
# This programs calculates the area and perimeter of a decagon given user input


import math



def main():
    # Code first greets user
    print("Hello! Welcome to Jayden's Decagon calculator")
    # This give the user input for the length
    side = float(input("What is the side length  of the decagon? (cm)"))
    # This makes the code stop if the User picks a negative number or zero.
    if side <= 0:
        print("Please pick a positive number!")
    else:
        area = 5 / 2 * (side**2) * math.sqrt(5 + 2 * math.sqrt(5))
        perimeter = 10 * side
        # This part of the code calculates the Area and Perimeter with the given input
        print("Area is {:.2f}cm^2".format(area))
        print("Perimeter is {:.2f}cm".format(perimeter))


if __name__ == "__main__":
    main()
