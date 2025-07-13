'''
Password Generator 

Key Features:
- Generates a strong random password of user-defined length
- User can include:
  - Capital letters (A–Z)
  - Numbers (0–9)
  - Special characters (!, @, #, etc.)
- Uses `random.choices()` for random selection
- Input taken from user for full customization

In Code:
- Uses basic Python lists to build the character pool
- Clean structure using `try-except` for error handling
Dependencies:
- random (built-in)

Example Inputs:
- Length: 12
- Capital: y
- Number: y
- Special char: y

Possible Output:
`A1d$M0bq25r!`

Developer: Rupankar Nag  
Last Update: 13-07-2025  


'''
import random

# n = length of password
# alphabign = use capital letters (True/False)
# numn = use numbers (True/False)
# scn = use special characters (True/False)
def passwordgenerator(n, alphabign, numn, scn):
    alphabig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    alphasmall = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    special_chars =['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',';', ':', "'", '"', '<', '>', ',', '.', '?', '/','~', '`']

    if alphabign:
        alphasmall += alphabig
    if numn:
        alphasmall += numbers
    if scn:
        alphasmall += special_chars


    return ''.join(random.choices(alphasmall, k=n))


if __name__ == "__main__":
    try:
        n = int(input("Enter length of password: "))
        x = input("Do you want capital letters? (y/n): ").strip().lower()
        alphabign = x != "n"

        y = input("Do you want numbers? (y/n): ").strip().lower()
        numn = y != "n"

        z = input("Do you want special characters? (y/n): ").strip().lower()
        scn = z != "n"

        password = passwordgenerator(n, alphabign, numn, scn)
        print(f"Your password is: {password}")
    except Exception as e:
        print("Error:", e)
