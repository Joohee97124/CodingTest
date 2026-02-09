from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque([(0,0)]) #value, index
    
    while que:
        value,index = que.popleft()
        
        if index == len(numbers):
            if value==target:
                answer +=1
        else:
            que.append((value+numbers[index], index+1))
            que.append((value-numbers[index], index+1))
            
    return answer