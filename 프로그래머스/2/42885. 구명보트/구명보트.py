def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    point1 = 0
    point2 = len(people)-1
    
    while True:
        if point1 > point2 :
            break
        if people[point1] + people[point2] <= limit:
            point2 -= 1
        answer += 1
        point1 += 1
            
    
    return answer