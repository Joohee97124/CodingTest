def solution(targets):
    answer = 0
    a,b = 0,0
    
    targets.sort(key=lambda x:x[1])
    a = targets[0][0]
    
    for c,d in targets:
        if c >= b:
            answer += 1
            a = c
            b = d
        
    return answer