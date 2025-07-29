def solution(num, total):
    answer = []
    tmp = total//num  #기준
    size = (num-1)//2 #이동거리
    
    for i in range(tmp-size , tmp-size+num):
        print(i)
        answer.append(i)
    
    return answer