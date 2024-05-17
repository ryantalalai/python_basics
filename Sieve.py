# Ryan Talalai
# 08 May 2021
# Sieve of Eratosthenes (Extra Credit)

lst = list(range(2,1000))

i = 1
while i < 999:
    q = i
    for j in range(2,lst[q]-1):
        if lst[q] % j == 0:
            lst.remove(lst[q])
        
    i += 1
    
print(lst)
        
    
