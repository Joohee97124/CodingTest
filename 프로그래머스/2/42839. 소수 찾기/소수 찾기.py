from itertools import permutations
def solution(numbers):
    answer = 0
    tmp = [0,1]
    
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers, i):
            if int(''.join(p)) not in tmp:
                tmp.append(int(''.join(p)))
    tmp.remove(0)
    tmp.remove(1)

    for t in tmp:
        answer += 1
        for i in range(2,t):
            if t%i==0:
                answer -= 1
                break
    
            
    return answer