def solution(num_list, n):
    
    number = (len(num_list)+1)//n
    return [num_list[i*n:i*n+n] for i in range(0, number)]