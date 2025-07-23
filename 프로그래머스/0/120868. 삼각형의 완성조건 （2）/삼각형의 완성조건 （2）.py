def solution(sides):
    sides.sort()
    
    #case 1
    #one = sides[1] - (sides[1] - sides[0])
    #case 2
    #two = sides[0]-1
    #answer = one + two
    
    return sides[0]*2 - 1