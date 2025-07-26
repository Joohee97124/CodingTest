def solution(score):
    #answer = []
    
    temp = [(eng+math)/2 for eng,math in score]
    #for eng,math in score:
    #    temp.append( (eng+math)//2 )
    
    temp.sort(reverse=True)
    
    #for eng,math in score:
    #    answer.append(temp.index((eng+math)/2)+1)
    #answer = [temp.index((eng+math)/2)+1 for eng,math in score]
    
    return [temp.index((eng+math)/2)+1 for eng,math in score]