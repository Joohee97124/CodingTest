def solution(array):
    #for ar in array:
    #    arr += str(ar)
    arr = ''.join([str(ar) for ar in array])
        
    #answer = arr.count('7')
    return arr.count('7')