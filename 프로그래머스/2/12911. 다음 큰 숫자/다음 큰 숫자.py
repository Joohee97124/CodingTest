def solution(n):
    none = str(bin(n)[2:]).count('1')
    
    while True:
        n += 1
        if none == str(bin(n)[2:]).count('1'):
            break 
            
    return n