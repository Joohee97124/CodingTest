def solution(emergency):
    '''
    answer = []
    dic = {}
    for i,emer in enumerate(emergency):
        dic[i] = emer
    sor = sorted(dic.values(), reverse=True)

    for emer in emergency:
        answer.append(sor.index(emer)+1)
    '''
    
    sor = sorted(emergency, reverse=True) 
    #nswer = [sor.index(emer)+1 for emer in emergency]
    return [sor.index(emer)+1 for emer in emergency]