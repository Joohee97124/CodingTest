def solution(arr, intervals):
    answer = [arr[a:b+1] for a,b in intervals]
    return [item for sub in answer for item in sub]