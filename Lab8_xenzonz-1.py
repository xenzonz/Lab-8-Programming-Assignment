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
     
     while True:
        upc_code: str = input("Enter 12 digit UPC-A code: ").strip()

        if len(upc_code) != 12:
            print("error must be 12 digits")
            continue
        
        if not upc_code.isdigit():
            print("error must be numbers only")
            continue

        return upc_code         
    

def find_upc(first_eleven_digits: str) -> int:
    
    odd_sum: int = 0
    even_sum: int = 0

    for i, digit in enumerate(first_eleven_digits):
        number: int = int(digit)

        if i % 2 == 0:
            odd_sum += number
        else:
            even_sum += number
    
    total: int = (odd_sum * 3) + even_sum
    check_digit: int = (10 - (total % 10)) % 10

    return check_digit






def main() -> None:
    
    upc_code: str = get_upc_input()

    first_eleven_digits: str = upc_code[:11]
    provided_check_digit: str = upc_code[11]

    expected_check_digit: int = find_upc(first_eleven_digits)

    print(f"\nThe first 11 digits are '{first_eleven_digits}'.")
    #print(upc_code)
    print(f"The provided check digit is '{provided_check_digit}'.")
    print("\nCalculating...")
    print(f"\nThe expected check digit is '{expected_check_digit}'.")

    if expected_check_digit == int(provided_check_digit):
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.")

    

if __name__ == "__main__":
    main()