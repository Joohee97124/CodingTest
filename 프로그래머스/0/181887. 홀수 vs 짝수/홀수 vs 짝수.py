def solution(num_list):
    tmp1 = 0 #홀수
    tmp2 = 0 #짝수
    
    for i,num in enumerate(num_list):
        if i%2==0:
            tmp1 += num
        else:
            tmp2 += num
    
    return max(tmp1, tmp2)