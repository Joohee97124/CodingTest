def solution(clothes):
    answer = 1
    hanger={}
    for a,b in clothes:
        hanger[b] = hanger.get(b,0) +1
    
    for k,v in hanger.items():
        answer *= (v+1)
    
    return answer-1