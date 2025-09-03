def solution(citations):
    citations.sort(reverse=True)
    
    for i,c in enumerate(citations):
        if (i+1) > c:
            return i
    
    return len(citations)
'''
입력값 〉 [5, 6, 7, 8]
기댓값 〉 4
'''