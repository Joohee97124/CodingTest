def solution(polynomial):
    score = polynomial.split(" + ")
    
    tmpx, tmps = 0, 0
    for sc in score:
        if 'x' in sc:
            if sc == 'x':
                tmpx += 1
            else:
                tmpx += int(sc[:-1])  # '3x' → 3, '10x' → 10
        else:
            tmps += int(sc)
    
    if tmpx and tmps:
        if tmpx==1:
            return f"x + {tmps}"
        else:
            return f"{tmpx}x + {tmps}"
    elif tmpx: 
        if tmpx==1:
            return f"x"
        else:
            return f"{tmpx}x"
    elif tmps:
        return f"{tmps}"