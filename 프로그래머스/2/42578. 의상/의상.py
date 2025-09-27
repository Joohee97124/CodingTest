def solution(clothes):
    answer = 1
    clothes_set = {}
    for cloth,types in clothes:
        clothes_set[types] = clothes_set.get(types,0)+1
    
    for cloth in clothes_set.values():
        answer *= (cloth+1)
    return answer-1