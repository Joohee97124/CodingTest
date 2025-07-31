def solution(n, control):
    #answer = 0
    dic = {"w":1, "s":-1, "d":10, "a":-10}
    
    #for con in control:
    #    answer += dic[con]
    
    #answer = sum([dic[con] for con in control])
    return n + sum([dic[con] for con in control])