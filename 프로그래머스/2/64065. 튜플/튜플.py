def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    
    x = [i.split(",") for i in s]
    x.sort(key=len)
    
    for i in x:
        for t in i:
            if int(t) not in answer:
                answer.append(int(t))
    
    return answer