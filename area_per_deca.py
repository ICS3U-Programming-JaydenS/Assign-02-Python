#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 6, 2025
# This program calculates the area and perimeter of a decagon given user input.

import math


def main():
    # Greets the user
    print("Hello! Welcome to Jayden's Decagon Calculator.")

    # Ask for the side length of the decagon
    side = float(input("What is the side length of the decagon? (in cm): "))

    # Checks if the side length is positive
    if side <= 0:
        print("Please pick a positive number!")
    else:
        # Calculate area and perimeter
        area = 5 / 2 * (side**2) * math.sqrt(5 + 2 * math.sqrt(5))
        perimeter = 10 * side

        # Print the results with formatted output
        print(f"Area is {area:.2f} cm^2")
        print(f"Perimeter is {perimeter:.2f} cm")


if __name__ == "__main__":
    main()
