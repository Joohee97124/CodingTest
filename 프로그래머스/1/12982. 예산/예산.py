def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    total = 0
    for bud in d:
        total += bud
        answer += 1
        if total > budget:
            answer -= 1
            break
    return answer