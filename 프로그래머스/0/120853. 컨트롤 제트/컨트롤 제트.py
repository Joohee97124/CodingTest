def solution(s):
    #answer = 0
    array = s.split(" ")
    
    final = []
    for i,arr in enumerate(array):
        if arr=='Z':
            final.pop(-1)
        else:
            final.append(int(arr))
    
    #for fin in final:
    #    answer += fin
    #answer = sum([fin for fin in final])
        
    return sum([fin for fin in final])