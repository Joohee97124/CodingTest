def solution(k, dungeons):
    answer = -1
    
    def dfs(k,visited,count):
        nonlocal answer
        answer = max(answer,count)
        
        for i in range(len(dungeons)):
            need,cost = dungeons[i]
            if not visited[i] and need <= k:
                visited[i] = True
                dfs(k-cost, visited, count+1)
                visited[i] = False
    
    dfs(k,[False]*len(dungeons), 0)
    return answer