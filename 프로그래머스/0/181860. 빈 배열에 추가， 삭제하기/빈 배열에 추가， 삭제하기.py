def solution(arr, flag):
    answer = []
    for i,fl in enumerate(flag):
        if fl :
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
                
    return answer