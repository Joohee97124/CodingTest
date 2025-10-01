def solution(answers):
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = {1:0, 2:0, 3:0}
    
    for i,an in enumerate(answers):
        o = one[i%len(one)]
        w = two[i%len(two)]
        h = three[i%len(three)]
        if an == o:
            score[1]+=1
        if an == w:
            score[2]+=1
        if an==h:
            score[3]+=1
    
    max_value = max(score.values())
    max_keys = [k for k,v in score.items() if v==max_value]
    
    return max_keys