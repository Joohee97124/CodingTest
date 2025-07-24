def solution(balls, share):
    #answer = 0
    def fact(n):
        if n==0 or n==1 :
            return 1
        return n*fact(n-1)
    
    #temp1 = fact(balls)
    #temp2 = fact(balls-share) * fact(share)
    #answer = temp1 // temp2
    return fact(balls) // (fact(balls-share) * fact(share))