def solution(num_list):
    odd = []
    even = []
    
    for num in num_list:
        even.append(num) if num%2==0 else odd.append(num)

    eve = ''.join(map(str,even))
    od = ''.join(map(str,odd))
    
    return int(eve) + int(od)
                                             
    