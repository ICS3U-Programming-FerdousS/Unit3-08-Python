#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: April 12, 2022
# This program asks the user for a year
# then check and tell them if
# it is a leap year or a noraml year.


def main():
    # ask users for a year as string
    string_year = input("Enter the year: ")
    # convert string input to int
    try:
        integer_year = int(string_year)
        print("")
         # check if user year is leap year or not and display ansers
        if (integer_year % 4 == 0):
            print(" it is a leap year!")
            if (integer_year % 100 == 0 and integer_year % 400 == 0):
                print(" it is a leap year!")
        elif (integer_year % 100 == 0):
            print(" it is not a leap year!")
        else:
            print(" it is not leap year!")
    # display invalid input
    except Exception:
        print("")
        print("invalid input")
 


if __name__ == "__main__":
    main()
