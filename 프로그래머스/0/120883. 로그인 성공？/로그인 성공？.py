def solution(id_pw, db):
    answer = 'fail'
    
    for b in db:
        if id_pw[0] == b[0]:
            answer = 'wrong pw'
            if id_pw[1] == b[1]:
                answer = 'login'
                
    return answer