# Name: Ryan Talalai
# Date: 23 February 2021
# Assignment: Alternate
# This program asks for a number n and outputs the alternating series of 1s and 0s

n = int(input("Enter n: "))

if n > 0:
    i = 1
    while i <= n:
        if((i % 2) == 1):
            print("1",end=" ")
        else:
            print("0",end=" ")

        i += 1
        
elif n <= 0:
    print("Invalid value")
