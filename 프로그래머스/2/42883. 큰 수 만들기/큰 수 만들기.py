def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and int(stack[-1]) < int(num) and k>0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k>0:
        stack = stack[:-k]
    answer = ''.join(stack)    
    return answer