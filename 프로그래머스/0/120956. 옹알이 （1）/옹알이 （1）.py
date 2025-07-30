def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        tmp = bab
        prev = ''
        
        while tmp :
            match = False
            for b in baby:
                if tmp.startswith(b):
                    tmp = tmp[len(b):]
                    prev = b
                    match = True
                    break
            if not match :
                break
        
        if tmp == '':
            answer += 1
                    
    return answer