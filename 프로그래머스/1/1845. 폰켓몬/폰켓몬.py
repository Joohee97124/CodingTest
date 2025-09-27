def solution(nums):
    k = len(nums)//2
    
    pocketmon = {}
    for num in nums:
        pocketmon[num] = pocketmon.get(num,0)+1
    
    return k if k < len(pocketmon) else len(pocketmon)