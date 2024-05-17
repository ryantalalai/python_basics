# Ryan Talalai
# 22 April 2021
# Timed Assignment

k = input('Please enter the list: ')
A = k.split()
n = int(input('Please enter n: '))
size = len(A)
     
for x in range(0, size-2):
         
    for y in range(x + 1, size-1):
                         
        for z in range(y + 1, size):
            if A[x] + A[y] + A[z] == n:
                print('Yes')
