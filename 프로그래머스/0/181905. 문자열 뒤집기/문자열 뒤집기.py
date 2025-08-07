def solution(my_string, s, e):
    tmp = ''.join([my_string[i] for i in range(e,s-1,-1)])
        
    return my_string[:s] + tmp + my_string[e+1:]