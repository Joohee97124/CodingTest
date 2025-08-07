def solution(a, d, included):
    tmp = [(a+i*d) for i in range(len(included))]
    return sum([t for t,i in zip(tmp, included) if i])