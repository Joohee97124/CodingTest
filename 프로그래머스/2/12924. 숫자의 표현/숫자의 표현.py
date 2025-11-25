def solution(n):
    answer = 0
    
    for i in range(1,n):
        tmp = i
        for j in range(i+1,n+1):
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
            else:
                tmp += j
        
            
    return answer+1