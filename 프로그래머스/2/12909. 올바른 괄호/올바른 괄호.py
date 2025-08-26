def solution(s):
    one = 0
    
    for i in s:
        if i=="(":
            one += 1
        else:
            if one>0: one-=1
            else: return False
    
    if one > 0 :
        return False
    return True
    