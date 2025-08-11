def solution(q, r, code):
    return ''.join([co for i,co in enumerate(code) if i%q==r])