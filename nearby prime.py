# Name: Ryan Talalai
# Date: 19 March 2021
# Assignment: Nearby Prime
# This program gives the prime number closest to n, or if equally close, the smaller is outputted

n = int(input("Enter n: "))

if n == 2 or n == 3:
    print("The prime closest to",n,"is",n)

elif n != 2:

    for i in range(2,n,1):
        if i % 2 != 0:
            x = i

    for j in range(n,1000000,1):
        if j % 2 != 0 and j < n +2:
            y = j


    for p in range(2,x,1):
        if x % p == 0:
            x -= 1
        else: lowprime = x

    for u in range(2,2*y,1):
        if y % u == 0:
            y += 1
        else: highprime = y


    if n - lowprime < highprime - n:
        print("The prime closest to",n,"is",lowprime)
    
    elif n - lowprime > highprime - n:
        print("The prime closest to",n,"is",highprime)

    elif n - lowprime == highprime - n:
        print("The prime closest to",n,"is",lowprime)
