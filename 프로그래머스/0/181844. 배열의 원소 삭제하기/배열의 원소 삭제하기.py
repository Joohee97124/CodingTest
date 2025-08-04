def solution(arr, delete_list):
    for delete in delete_list:
        if delete in arr:
            arr.remove(delete)
            
    answer = [a for a in arr if a not in delete_list]
    
    return answer