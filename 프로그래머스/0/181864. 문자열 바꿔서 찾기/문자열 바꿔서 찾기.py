def solution(myString, pat):
    answer = 0
    tmp = ''
    
    # A->B B->A 바꿔주기
    for my in myString:
        tmp += 'B' if my=='A' else 'A'

    # pat 찾아주기
    size = len(tmp) - len(pat)
    for i in range(0, size+1):
        answer = 1 if tmp[i:i+len(pat)] == pat else 0
        if answer == 1: break
    
    return answer