# Ryan Talalai
# 07 May 2021
# Final
# Just run and enter list with each number separated by comma

# Part 1
def palin(x):
    num = str(x)
    pal = ""
    for i in num:
       pal = i + pal
    if num == pal:
        return True
    else:
        return False


# Part 2
def nearprime(x):
    k = 0
    for i in range(1,int(x+1)):
        if (x % i) == 0:
            k += 1
    if k <= 4:
        return True
    else:
        return False

# Part 3
def updown(x):
    up = False
    down = False
    updown = False
    d = [int(y) for y in str(x)]
    q = 0

    for i in range(0,len(d)-1):
        if d[i] <= d[i+1]:
            up = True
        else:
            up = False
            break
    for j in range(0,len(d)-1):
        if d[j] >= d[j+1]:
            down = True
        else:
            down = False
            break
    for z in range(0,len(d)-1):
        if d[z] <= d[z+1]:
            updown = True
            q += 1
        else:
            updown = False
            break
    for z in range(q,len(d)-1):
        if d[z] >= d[z+1]:
            updown = True
        else:
            updown = False
            break
        
    if up == True:
        return True
    elif down == True:
        return True
    elif updown == True:
        return True
    elif x == 1:
        return True
    else:
        return False

def main():
    u = input("Please Enter List: ")
    lst = u.split(',')
    for j in range(len(lst)):
        lst[j] = int(lst[j])
    n = int(input("Please Enter Position: "))
    lst2 = []
    lst3 = []
    for i in range(0,len(lst)):
        score = lst[i]
        if palin(lst[i]) == True:
            score = 2*score
        if nearprime(lst[i]) == True:
            score = 2*score
        if updown(lst[i]) == True:
            score = 3*score
        lst2.append(score)

    lst3 = [x for _,x in sorted(zip(lst2,lst))]
    lst4 = []
    for p in range(0,len(lst3)):
        score = lst3[p]
        if palin(lst3[p]) == True:
            score = 2*score
        if nearprime(lst3[p]) == True:
            score = 2*score
        if updown(lst3[p]) == True:
            score = 3*score
        lst4.append(score)

    
    print(lst3[n]) 
    print(lst4[n])

main()



