def solution(nums):
    answer = 0
    count = 0
    tmp = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                tmp.append(nums[i]+nums[j]+nums[k])
                
    for t in tmp:
        for r in range(2,t):
            if t%r==0:
                count+=1
        if count == 0:
            answer += 1
        count = 0 
        
    return answer