def solution(n,a,b):
    answer = 1
    
    while True:
        if (a+1)//2 == (b+1)//2:
            break
        
        a = a//2 if a%2==0 else (a+1)//2
        b = b//2 if b%2==0 else (b+1)//2
        
        answer += 1
            
    return answer