def solution(M, N):
    #answer = 0
    
    # case1) M 자르기
    #answer += (M-1)
    # case2) N 자르기
    #answer += (N-1) *2
    
    #answer = (M-1) + ((N-1) *2)
    return (M-1) + ((N-1) *M)