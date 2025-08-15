def solution(spell, dic):
    answer = 2
    for di in dic:
        if sorted(di) == sorted(spell):
            answer = 1
            break
    return answer