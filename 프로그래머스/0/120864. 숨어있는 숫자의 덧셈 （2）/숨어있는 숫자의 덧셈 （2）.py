def solution(my_string):
    answer = 0
    temp = ''
    
    for my in my_string:
        if my.isdigit():
            temp += my
        elif len(temp)>0:
            answer += int(temp)
            temp = ''
    
    if len(temp)>0:
        answer += int(temp)
    return answer