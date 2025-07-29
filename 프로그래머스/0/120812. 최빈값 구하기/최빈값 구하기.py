def solution(array):
    dic = {}
    
    for arr in array:
        dic[arr] = 0
    
    for arr in array:
        dic[arr] += 1
    
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    if len(dic)>1 and dic[0][1] == dic[1][1]:
        return -1
    else:
        return dic[0][0]