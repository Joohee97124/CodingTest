def solution(num_list):
    tmp = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            tmp *= num
        return tmp