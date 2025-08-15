def solution(emergency):
    answer = [0] * len(emergency)
    tmp = sorted(emergency, reverse=True)
    
    for i,t in enumerate(tmp):
        answer[emergency.index(t)] = (i+1)
    return answer