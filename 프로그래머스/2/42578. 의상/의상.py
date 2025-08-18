def solution(clothes):
    answer = 1
    cl = {}
    for a,b in clothes:
        cl[b] = cl.get(b,0) +1
    
    for k,v in cl.items():
        answer *= (v+1)
    
    return answer-1