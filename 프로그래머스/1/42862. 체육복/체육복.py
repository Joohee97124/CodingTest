def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    lost_set = set(lost)-set(reserve)
    reserve_set = set(reserve)-set(lost)
    
    for l in list(lost_set):
        if (l-1) in reserve_set:
            lost_set.remove(l)
            reserve_set.remove(l-1)
        elif (l+1) in reserve_set:
            lost_set.remove(l)
            reserve_set.remove(l+1)
    return n - len(lost_set)