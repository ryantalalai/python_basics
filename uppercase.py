# Name: Ryan Talalai
# Date: 16 February 2021
# Assignment: Uppercase
# This program asks for a character and returns the uppercase of the character

ch = input("Please enter a character ")

if ord(ch) >= 65 and ord(ch) <= 90:
    print("The uppercase is",ch)

elif ord(ch) >= 97 and ord(ch) <= 122:
    y = ord(ch) - 32
    print("The uppercase is",chr(y))

elif ord(ch) > 122:
    print("You didn't enter an alphabet")

elif ord(ch) < 65:
    print("You didn't enter an alphabet")

elif ord (ch) > 90 and ord(ch) < 97:
    print("You didn't enter an alphabet")

