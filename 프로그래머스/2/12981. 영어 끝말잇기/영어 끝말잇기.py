def solution(n, words):
    indexs = 0
    
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            indexs = i+1
            break
    
    first = n if indexs > 0 and indexs%n==0 else indexs%n
    second = indexs//n+1 if indexs%n>0 else indexs//n

    return [first,second]