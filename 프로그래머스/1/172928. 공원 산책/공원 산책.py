def solution(park, routes):
    #n 높이(y) m 길이(x)
    n = len(park)
    m = len(park[0])
    answer = [0,0] #y,x (S+1 N-1 E+1 W-1)
    
    for index,pa in enumerate(park):
        if 'S' in pa:
            answer = [index,pa.index('S')]
            break
    
    for route in routes:
        way,num = route.split(" ")
        move_flag = True
        ny,nx = answer
        
        for i in range(int(num)):
            if way=='E': nx+=1
            elif way=='W': nx-=1
            elif way=='S': ny+=1
            elif way=='N': ny-=1
            
            if nx<0 or m<=nx or ny<0 or n<=ny or park[ny][nx]=='X':
                move_flag = False
                break
        
        if move_flag:
            answer = [ny,nx]
        
    return answer