# Ryan Talalai
# 07 May 2021
# Final

# Part 2: Near Prime

def nearprime(x):
    k = 0
    for i in range(1,int(x+1)):
        if (x % i) == 0:
            k += 1
    if k <= 4:
        return True
    else:
        return False

print(nearprime(19925))
