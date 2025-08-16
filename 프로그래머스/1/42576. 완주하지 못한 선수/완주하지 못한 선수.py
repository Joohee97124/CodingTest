def solution(participant, completion):
    dic = {}
    for par in participant:
        dic[par] = dic.get(par, 0) +1
    
    for com in completion:
        dic[com] -= 1  
    
    for k,v in dic.items():
        if v > 0:
            return k
