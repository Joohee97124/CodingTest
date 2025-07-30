def solution(board):
    answer = 0
    # 상 하 좌 우 좌상대 우상대 좌하대 우하대
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    
    #danger = []
    #for i in range (len(board)):
    #    tmp = [0] * len(board)
    #    danger.append(tmp)
    danger = [[0] * len(board) for i in range(len(board))]
    
    for i,row in enumerate(board):
        for j,value in enumerate(row):
            if value==1:
                danger[i][j]=1
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<=ni<len(board) and 0<=nj<len(board):
                        danger[ni][nj]=1
    
    for i,row in enumerate(danger):
        for j,value in enumerate(row):
            if value == 0 :
                answer += 1
    
    return answer
#1 1이 어디에 있는지 찾는다 (인덱스를)
#2 1의 양옆 / 위아래 / 대각선 을 1로 바꾼다
#3 0의 개수를 return 한다
'''
[[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0]]
'''