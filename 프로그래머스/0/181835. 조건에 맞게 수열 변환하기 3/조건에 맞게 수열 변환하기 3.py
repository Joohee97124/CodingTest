def solution(arr, k):
    answer = []
    
    for ar in arr:
        answer.append((ar+k) if k%2==0 else (ar*k) )
        '''
        if k%2==0:
            answer.append(ar+k)
        else:
            answer.append(ar*k)
        '''
    return answer