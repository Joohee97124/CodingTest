def solution(nums):
    phone = {}
    for num in nums:
        phone[num] = phone.get(num,0) +1
    
    return len(phone) if (len(nums)//2) > len(phone) else (len(nums)//2)