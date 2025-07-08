def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        arr = list(str(num))
        answer += arr.count(str(k))
    return answer