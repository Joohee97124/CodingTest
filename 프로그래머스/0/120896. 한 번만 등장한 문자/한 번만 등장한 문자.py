def solution(s):
    answer = ''
    #for i in list(s):
    #    if s.count(i)==1:
    #        answer += i
    #answer = ''.join(sorted(answer))
    
    #answer = ''.join(sorted([i for i in list(s) if s.count(i)==1]))
    return ''.join(sorted([i for i in list(s) if s.count(i)==1]))