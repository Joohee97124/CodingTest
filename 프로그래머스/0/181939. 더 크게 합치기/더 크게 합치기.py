def solution(a, b):
    ab = ''.join([str(a), str(b)])
    ba = ''.join([str(b), str(a)])
    
    return max(int(ab), int(ba))