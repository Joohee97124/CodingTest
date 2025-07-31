def solution(my_strings, parts):
    #answer = ''
    #for i, (a,b) in enumerate(parts):
    #    answer += my_strings[i][a:b+1]
    
    #answer = ''.join([my_strings[i][a:b+1] for i,(a,b) in enumerate(parts)])
    return ''.join([my_strings[i][a:b+1] for i,(a,b) in enumerate(parts)])