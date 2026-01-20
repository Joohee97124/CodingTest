from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        answer += 1
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.popleft()
        people.pop()
    return answer