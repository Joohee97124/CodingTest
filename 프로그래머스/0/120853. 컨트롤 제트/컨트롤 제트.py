def solution(s):
    answer = 0
    array = s.split(" ")
    
    final = []
    for i,arr in enumerate(array):
        if arr=='Z':
            answer -= int(array[i-1])
            #final.pop(-1)
        else:
            answer += int(arr)
            #final.append(int(arr))
            
    return answer    
    #return sum([fin for fin in final])