def solution(dots):
    a,b,c,d = dots
    
    if (a[1]-b[1])*(c[0]-d[0]) == (c[1]-d[1])*(a[0]-b[0]):
        return 1
    elif (a[1]-c[1])*(b[0]-d[0]) == (b[1]-d[1])*(a[0]-c[0]):
        return 1
    elif (a[1]-d[1])*(b[0]-c[0]) == (b[1]-c[1])*(a[0]-d[0]):
        return 1
    else:
        return 0

'''
12 / 34
13 / 24
14 / 23
'''