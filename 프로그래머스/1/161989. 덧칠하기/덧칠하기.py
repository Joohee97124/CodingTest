def solution(n, m, section):
    answer = 1
    tmp = section[0]
    
    for sec in section:
        if tmp+m <= sec :
            tmp = sec
            answer += 1
    
    return answer

# section을 돌면서 tmp+m 보다 크면 +1 해주고 tmp 업데이트
