def solution(s):
    count = 0
    for i in s:
        if i=='(':
            count += 1
        elif i==')' and count <=0 :
            return False
        elif i==')' and count > 0 :
            count -= 1
    
    if count ==0 and s[0]=='(':
        return True
    else:
        return False
    