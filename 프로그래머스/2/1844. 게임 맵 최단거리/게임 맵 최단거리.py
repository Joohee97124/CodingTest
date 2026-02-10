from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) #행
    m = len(maps[0]) #열
    que = deque([(0,0)])
    #오왼상하
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]

    while que:
        x,y = que.popleft()
        for i in range(4):
            tmpx = x+nx[i]
            tmpy = y+ny[i]
            if 0<=tmpx<n and 0<=tmpy<m and maps[tmpx][tmpy]!=0:
                if maps[tmpx][tmpy] == 1:
                    maps[tmpx][tmpy] = maps[x][y]+1
                    que.append((tmpx,tmpy))
        
    answer = maps[n-1][m-1]
    if answer==1:
        return -1
    else:
        return answer