def solution(binomial):
    bino = binomial.split(" ")
    if bino[1]=='+':
        return int(bino[0]) + int(bino[2])
    elif bino[1]=='-':
        return int(bino[0]) - int(bino[2])
    elif bino[1]=='*':
        return int(bino[0]) * int(bino[2])