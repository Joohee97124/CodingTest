def solution(record):
    answer = []
    nameset = {}
    act = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    
    for rec in record:
        if rec.startswith("Enter") or rec.startswith("Change"):
            action,ID, name = rec.split(" ")
            nameset[ID] = name
    
    for rec in record:
        if rec.startswith("Enter"):
            action,ID, name = rec.split(" ")
            answer.append(nameset[ID] + act[action])
        elif rec.startswith("Leave"):
            action,ID = rec.split(" ")
            answer.append(nameset[ID] + act[action])
            
    
    return answer