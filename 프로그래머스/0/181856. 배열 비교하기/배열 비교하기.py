def solution(arr1, arr2):
    answer = 0
    tmp1 = 0
    tmp2 = 0
    
    if len(arr1)>len(arr2):
        return 1
    elif len(arr2)>len(arr1):
        return -1
    else:
        for i in range(len(arr1)):
            tmp1 += arr1[i]
            tmp2 += arr2[i]
        if tmp1 > tmp2:
            return 1
        elif tmp2 > tmp1 :
            return -1
        else:
            return 0
    return answer