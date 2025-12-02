def solution(s) :
    count, zero = 0 ,0
    
    while s != '1':
        count += 1
        zero += s.count('0')
        
        tmp = s.count('1')
        s = bin(tmp)[2:]
        
    return [count, zero]