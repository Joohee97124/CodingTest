from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]
    
    # BFS 함수
    def bfs(start_pos,find):
        visited =[[-1]*m for _ in range(n)]
        
        que = deque()
        que.append(start_pos)
        visited[start_pos[0]][start_pos[1]] = 0
        
        while que:
            x,y = que.popleft()
            if maps[x][y] == find:
                return visited[x][y], (x,y)
            
            for i in range(4):
                tmpx = x+nx[i]
                tmpy = y+ny[i]
                if 0<=tmpx<n and 0<=tmpy<m:
                    if maps[tmpx][tmpy]!='X' and visited[tmpx][tmpy]==-1:
                        visited[tmpx][tmpy] = visited[x][y] + 1
                        que.append((tmpx,tmpy))
        return -1, (-1,-1)
    
    # S찾기
    for r,row in enumerate(maps):
        if 'S' in row:
            start = (r, row.index('S'))
            break
    # S->L
    time1, startS = bfs(start, 'L')
    if time1==-1: return -1
    # L->E
    time2, startL = bfs(startS, 'E')
    if time2==-1: return -1
    return time1+time2