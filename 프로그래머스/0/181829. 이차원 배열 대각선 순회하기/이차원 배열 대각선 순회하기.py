def solution(board, k):          
    return sum([b for i,boa in enumerate(board) for j,b in enumerate(boa) if i+j <= k])