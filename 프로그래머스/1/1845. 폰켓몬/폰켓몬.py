def solution(nums):
    pho={}
    for n in nums:
        pho[n] = pho.get(n,0) +1
        
    return len(nums)//2 if len(nums)//2 < len(pho) else len(pho)
    
    