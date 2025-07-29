# 이문제에서는 eval() 함수에 대해 알게 되었음
def solution(quiz):
    answer = []
    
    for qu in quiz:
        q = qu.split(" = ")
        tmp = eval(q[0])
        
        if tmp == int(q[1]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer