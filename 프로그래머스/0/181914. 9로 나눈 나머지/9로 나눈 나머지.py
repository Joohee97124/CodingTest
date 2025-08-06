def solution(number):
    answer = 0
    while int(number) >= 10:
        answer = sum([int(i) for i in number])
        number = str(answer)
    
    if answer%9==0:
        return 0 
    return answer