def solution(my_string, m, c):
    my = [my_string[i*m : i*m+m] for i in range(len(my_string)//m)]
    
    return ''.join([m[c-1] for m in my])