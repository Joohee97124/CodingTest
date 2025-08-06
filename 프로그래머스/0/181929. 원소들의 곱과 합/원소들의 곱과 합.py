def solution(num_list):
    tmp1 = 1
    for num in num_list:
        tmp1 *= num
    tmp2 = sum(num_list) 
    
    return 0 if tmp1 > tmp2*tmp2 else 1