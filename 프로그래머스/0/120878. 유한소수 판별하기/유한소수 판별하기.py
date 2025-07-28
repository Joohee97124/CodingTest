def solution(a, b):
    tmp = 0
    
    # 1
    for i in range(2,a+1):
        if a%i==0 and b%i==0:
            tmp = i

    if tmp>0:
        b = b//tmp

    #2
    while b%2==0:
        b = b//2
    while b%5==0:
        b = b//5
    
    #if b==1 :
    #    return 1
    #else:
    #    return 2
    return 1 if b == 1 else 2

'''
1. a b의 공약수로 b를 나누기
2. b의 소인수가 2,5인지 확인 
'''