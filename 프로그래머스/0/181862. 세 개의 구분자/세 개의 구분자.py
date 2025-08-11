def solution(myStr):
    answer = []
    myStr = myStr.replace('b','a')
    myStr = myStr.replace('c','a')
    
    tmp = myStr.split('a')
    
    for my in tmp:
        if my != '':
            answer.append(my)
            
    if not answer:
        answer.append('EMPTY')
    return answer