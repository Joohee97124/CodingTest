from collections import deque
def solution(cacheSize, cities):
    #1. que에 cacheSize 만큼 기본값 초기화 해놓기
    answer = 0
    que = deque()

    #2. cities 를 돌면서 que 설정해
    for city in cities:
        city = city.lower()
        
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            que.append(city)
            if len(que) > cacheSize:
                que.popleft()
    
    
    return answer