def solution(s):
    stack = []
    
    for sc in s:
        if len(stack)==0:
            stack.append(sc)
        elif stack[-1] == sc:
            stack.pop()
        else:
            stack.append(sc)
    
    return 1 if len(stack)==0 else 0
