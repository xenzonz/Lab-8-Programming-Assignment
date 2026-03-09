print("hello world")

"""
Docstring for Lab8_xenzonz_1
i. LAB 8: UPC Validator
ii. Sam Cocquyt
iii.  Program that validates a 12-digit UPC-A code. 
    The program will ask the user for a 12-digit UPC, use a function to calculate the correct check digit, and then inform the user if the full UPC is valid.
    Has input validation. Before calling the find_UPC() function, check that the user's input is exactly 12 characters long and contains only numbers. 
    If the input is invalid, print an error and ask again.
iv. No starter code
    Algorithm: en.wikipedia.org/wiki/Universal_Product_Code#Check_digit_calculation
v. 3/8/2026
"""

def get_input():
     
     while True:
        upc_code: str = input("Enter 12 digit UPC-A code: ")

        if len(upc_code) != 12:
            print("error must be 12 digits")
            continue
        
        if not upc_code.isdigit():
            print("error must be numbers only")
            continue

        return upc_code

get_input()         
    

def find_upc():
    return 0

def main():
    return 0