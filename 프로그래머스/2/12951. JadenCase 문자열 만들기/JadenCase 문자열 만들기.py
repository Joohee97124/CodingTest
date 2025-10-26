def solution(s):
    #입력값 〉   "  for the what  1what  "
    #기댓값 〉   "  For The What  1what  "
    answer = ''
    for i in range(0,len(s)):
        if s[i] == ' ' or s[i].isdigit():
            answer += s[i]
        else:
            if i==0 or s[i-1]==' ':
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        

    return answer