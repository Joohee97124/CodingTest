def solution(brown, yellow):
    answer = []
    total = brown + yellow
    tmp = []
    
    for i in range(2,int(total ** 0.5)+1):
        if total%i == 0:
            tmp.append([i,total//i])
    
    for a,b in tmp:
        if (a-2)*(b-2)==yellow:
            answer.extend([b,a])
            break
            
    return answer