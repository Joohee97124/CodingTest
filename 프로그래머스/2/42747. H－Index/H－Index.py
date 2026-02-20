def solution(citations):
    l = len(citations)
    citations.sort()
    print(citations)
    
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0