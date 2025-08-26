from math import ceil
def solution(progresses, speeds):
    answer = []
    day = [ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    print(day)
    
    tmp = day[0] #이전의 day
    count = 0 #배포수
    for d in day:
        if d <= tmp:
            count += 1
        else:
            answer.append(count)
            count = 1
            tmp = d
    
    answer.append(count)
    return answer