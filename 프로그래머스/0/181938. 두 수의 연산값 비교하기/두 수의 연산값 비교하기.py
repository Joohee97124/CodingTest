def solution(a, b):
    ab = ''.join([str(a),str(b)])
    return max(int(ab), 2*a*b)