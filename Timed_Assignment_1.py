# Ryan Talalai
# 04 April 2021
# Timed Assignment 01

elements = []
n = int(input("Please enter number of elements in list: "))

for i in range (0,n):
    y = int(input("Enter Element: "))
    elements.append(y)

print("You entered:",elements)

elements1 = []
elements2 = []
x = len(elements)

j = 0
while (j < x/2):
    elements1.append(elements[j])
    j += 1

i = x -1
while (i >= n/2):
    elements2.append(elements[i])
    i -= 1

elements2.sort()
elements1.append(elements2)

print("Sorted:",elements1)
