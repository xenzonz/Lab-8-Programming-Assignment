#print("hello world")

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


def get_upc_input() -> str:
    """
    Prompt the user until a valid 12-digit UPC-A code is entered.

    Returns:
        str: A valid 12-digit UPC-A code entered by the user.
    """
    while True:
        upc_code: str = input("Enter 12 digit UPC-A code: ").strip()

        #print error if input is not 12 digits long
        if len(upc_code) != 12:
            print("Error: UPC must be exactly 12 digits long\n")
            continue
        
        #print error if input is not digits only
        if not upc_code.isdigit():
            print("Error: UPC must contain only numbers\n")
            continue

        return upc_code         
    

def find_upc(first_eleven_digits: str) -> int:
    """
    Calculate the expected UPC-A check digit from the first 11 digits.

    Args:
        first_eleven_digits (str): The first 11 digits of a UPC-A code.

    Returns:
        int: The calculated check digit.
    """
    
   
    odd_sum: int = 0
    even_sum: int = 0

    #loop each digit one at a time
    for i, digit in enumerate(first_eleven_digits):

        #convert digit from a string to an int
        number: int = int(digit)

        #add digits in odd position to odd_sum
        if i % 2 == 0:
            odd_sum += number
        else: #add digits in even position to even_sum
            even_sum += number
    
    #check digit calculation via wikipedia
    total: int = (odd_sum * 3) + even_sum
    check_digit: int = (10 - (total % 10)) % 10

    return check_digit






def main() -> None:
    """
    Get a UPC-A code from the user, calculate the expected check digit,
    and display whether the UPC is valid or invalid.
    """
     
    upc_code: str = get_upc_input()

    first_eleven_digits: str = upc_code[:11] #first 11 digits
    provided_check_digit: str = upc_code[11] #last digit entered by user

    expected_check_digit: int = find_upc(first_eleven_digits) #calculate what the last digit should be

    print(f"\nThe first 11 digits are '{first_eleven_digits}'.")
    print(f"The provided check digit is '{provided_check_digit}'.")

    print("\nCalculating...")
    
    print(f"\nThe expected check digit is {expected_check_digit}.")

    #check if UPC is valid
    if expected_check_digit == int(provided_check_digit):
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.")

    
#main guard
if __name__ == "__main__":
    main()