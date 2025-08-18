def solution(participant, completion):
    person = {}
    for part in participant :
        person[part] = person.get(part,0) +1
    
    for com in completion:
        person[com] -= 1
    
    for k,v in person.items():
        if v > 0 :
            return k