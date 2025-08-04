def solution(num_list, n):
    count = num_list.count(n)
    if count >= 1:
        return 1
    else:
        return 0