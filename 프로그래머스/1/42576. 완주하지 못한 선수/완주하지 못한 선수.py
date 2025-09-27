def solution(participant, completion):
    par = {}
    
    for p in participant:
        par[p] = par.get(p,0)+1
    
    for com in completion:
        if com in par:
            par[com] -= 1
    
    for k,v in par.items():
        if v>0:
            return k
    