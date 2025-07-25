def solution(keyinput, board):
    dx = 0
    dy = 0

    #dir = {"up": 0, "down": 1, "left": 2, "right": 3}
    #x = [0,0,-1,1]
    #y = [1,-1,0,0]

    for key in keyinput:
        if key=='up' and board[1]//2 > dy :
            dy += 1
        elif key=='down' and -(board[1]//2) < dy : 
            dy -= 1
        elif key=='right' and board[0]//2 > dx :
            dx += 1
        elif key=='left' and -(board[0]//2) < dx:
            dx -=1
    
    #answer = [dx,dy]
    return [dx,dy]