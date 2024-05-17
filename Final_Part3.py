# Ryan Talalai
# 07 May 2021
# Final

# Part 3: Updown

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


