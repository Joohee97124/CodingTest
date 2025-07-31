def solution(numLog):
    #answer = ''
    #tmp = []
    dic = {1:"w", -1:"s", 10:"d", -10:"a"}
    
    #for i in range(len(numLog)-1):
    #    tmp.append(numLog[i+1] - numLog[i])
    tmp = [numLog[i+1] - numLog[i] for i in range(len(numLog)-1)]
    
    #for word in tmp:
    #    answer += dic[word]
    #answer = ''.join([dic[word] for word in tmp])   
    return ''.join([dic[word] for word in tmp])