# Ryan Talalai
# 29 April 2021
# Timed Assignment 03


def lsearch(x,lst):
    j = 0
    while j < len(lst):
        if lst[j] == x:
            print(x,end= ' ')
        j += 1
    

def main():
    a = input("Please enter A: ")
    lst = [int(i) for i in a.split()]
    b = int(input("Please enter B: "))
    print("The good numbers present are",end=' ')

    i = 1
    while i < 1000000:
        y = b**i
        lsearch(y,lst)
        i += 1

main()
