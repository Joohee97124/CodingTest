def solution(strArr):
    
    return [arr.upper() if i%2==1 else arr.lower() for i,arr in enumerate(strArr) ]