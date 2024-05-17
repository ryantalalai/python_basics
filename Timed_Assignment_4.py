# Ryan Talalai
# 05 May 2021
# Timed Assignment 04

def course():
    i = 0
    while i < n:
        k = int(input("Enter course {}: ".format(i+1)))
        z = int(input("Enter prerequisite {}: ".format(i+1)))
        lst.append(k)
        lst2.append(z)
        i += 1

def sem():
    j = 1
    while j < n:
        c = int(input("Enter sem {} course: ".format(j)))
        lst3.append(c)
        j += 1

def check():
    q = 0
    while q < n:
        g = lst3[q]
        a = 0
        while a < n:
            if lst[a] == g and lst[a] > lst2[a]:
                global x
                x == 1
            a += 1
        q += 1
        

def main():
    n = int(input("Enter number of courses: "))
    lst = []
    lst2 = []
    lst3 = []
    x = 0
    course()
    sem()
    check()
    if x == 0:
        print("Yes its possible to take it in that order")
    if x == 1:
        print("No its not possible to take it in that order")

main()


