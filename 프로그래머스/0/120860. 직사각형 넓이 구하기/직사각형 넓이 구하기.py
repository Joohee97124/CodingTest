def solution(dots):
    #answer = 0
    xlen = max(x[0] for x in dots) - min(x[0] for x in dots)
    ylen = max(x[1] for x in dots) - min(x[1] for x in dots)
    
    #answer = xlen*ylen
    return xlen*ylen