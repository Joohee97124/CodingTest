def solution(numlist, n):
    answer = []
    numdic = {}
    for num in numlist:
        numdic[num] = abs(n-num)
    
    numdic = sorted(numdic.items(), key=lambda x:(x[1], -x[0]))
    
    for key,value in numdic:
        answer.append(key)
    return answer