def solution(n):
    arr = [0] * n
    
    for i in range(0,n):
        if i==0 or i==1:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n-1]%1234567