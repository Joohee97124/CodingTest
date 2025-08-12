def solution(arr):
    tmp = []
    for i,ar in enumerate(arr):
        if ar==2:
            tmp.append(i)
            break
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==2:
            tmp.append(i)
            break
    
    if not tmp :
        return [-1]
    elif len(tmp) == 1:
        return [2]
    else:
        a,b = tmp
        return arr[a:b+1]
    