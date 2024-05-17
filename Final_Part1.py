# Ryan Talalai
# 07 May 2021
# Final

# Part 1: Palindrome

def palin(x):
    num = str(x)
    pal = ""
    for i in num:
       pal = i + pal
    if num == pal:
        return True
    else:
        return False


