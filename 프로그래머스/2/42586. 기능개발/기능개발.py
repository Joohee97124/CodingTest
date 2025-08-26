from math import ceil
def solution(progresses, speeds):
    answer = []
    day = [ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    print(day)
    
    tmp = day[0] #이전의 day
    count = 0 #배포수
    for d in day:
        if d <= tmp:
            print(d)
            count += 1
            print('count', count)
        else:
            answer.append(count)
            count = 1
            print('answer', answer)
            tmp = d
        print(d,' , ', tmp)
    
    answer.append(count)
    return answer