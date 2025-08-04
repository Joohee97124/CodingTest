def solution(str_list, ex):
    #answer = ''.join([st for st in str_list if ex not in st])
    #for st in str_list:
    #    if ex not in st:
    #        answer += st

    return ''.join([st for st in str_list if ex not in st])