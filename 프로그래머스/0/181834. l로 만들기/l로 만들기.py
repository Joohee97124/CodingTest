def solution(myString):
    answer = ''
    for my in myString:
        answer += ('l' if ord(my) < ord('l') else my)
        '''
        if ord(my) < ord('l'):
            answer += 'l'
        else:
            answer += my
        '''
    return answer