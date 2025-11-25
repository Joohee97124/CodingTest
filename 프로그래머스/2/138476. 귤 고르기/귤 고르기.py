def solution(k, tangerine):
    answer = 0
    ora = {}
    
    # dict
    for tan in tangerine:
        ora[tan] = ora.get(tan, 0) +1
    
    # sort
    ora_d = dict(sorted(ora.items(), 
                        key= lambda x:x[1], reverse=True))
    
    # answer 
    for key,value in ora_d.items():
        if k<=0:
            break
        else:
            answer +=1
            k -= value
    
    return answer
    # dict sort 