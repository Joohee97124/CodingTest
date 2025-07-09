def solution(n):
    #반복문 사용
    answer = 0
    temp = 1
    for i in range(1, 11):
        temp *= i
        
        if temp > n :
            answer = i-1
            break
        elif temp == n :
            answer = i
            break
    return answer

    '''재귀함수 사용
    def fact(k, acc):
        if acc > n:
            return k-1
        elif acc == n:
            return k
        else:
            return fact(k+1, acc * (k+1))
            
    return fact(1,1)
    '''