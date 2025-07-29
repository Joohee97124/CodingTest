def solution(numer1, denom1, numer2, denom2):
    #answer = []
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    def gcd(a, b):
        while b:
            a,b = b , a%b
        return a
    
    g = gcd(denom, numer)
    #answer = [numer//g , denom//g]
    
    return [numer//g , denom//g]
# 1. 분모를 서로 곱해 (분자도)
# 2. 더하고
# 3. 최종값에서 분자와 분모를 최대 공약수로 나누셈
''' 최대 공약수 찾기 : 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
'''