def solution(n):
    arr = [0] * n
    
    for index in range(0,n):
        if index==0:
            arr[index] = 1
        elif index==1:
            arr[index] = 2
        else:
            arr[index] = arr[index-1] + arr[index-2]
            
    return arr[n-1] % 1234567     

