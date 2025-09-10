from itertools import permutations
def solution(k, dungeons):
    answer = 0
    orders = permutations(dungeons,len(dungeons))
    
    for order in orders:
        tmp, stemina = 0, k
        for a,b in order:
            if a <= stemina:
                tmp += 1
                stemina -= b
            else:
                break
        answer = max(answer, tmp)     
    return answer