def solution(spell, dic):
    answer = 2
    
    spell = sorted(spell)
    for word in dic :
        word = sorted(word)
        print(word)
        if word == spell:
            answer = 1
            
    return answer