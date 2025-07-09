def solution(array, n):
    temp = [abs(arr-n) for arr in array]
    temp.sort()
    
    if (n-temp[0]) in array:
        return (n - temp[0])
    else:
        return (n + temp[0])