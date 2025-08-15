def solution(my_string):
    answer = 0
    tmp = ''
    
    for my in my_string:
        if my.isdigit():
            tmp+=my
        else:
            if tmp:
                answer += int(tmp)
                tmp = ''
        
    if tmp:
        answer += int(tmp)

    return answer