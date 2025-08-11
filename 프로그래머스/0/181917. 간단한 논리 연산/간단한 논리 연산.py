def solution(x1, x2, x3, x4):
    tmp1, tmp2 = True, True
    
    if x1 == False and x2==False:
        tmp1 = False
    else:
        tmp1 = True
    
    if x3 == False and x4==False:
        tmp2 = False
    else:
        tmp2 = True
    
    print(tmp1, tmp2)
    if tmp1==True and tmp2==True:
        return True
    else:
        return False