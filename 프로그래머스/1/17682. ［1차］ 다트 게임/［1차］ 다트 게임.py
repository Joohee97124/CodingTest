def solution(dartResult):
    num = ''
    scorelist = []
    SDT = {'S':1, 'D':2, 'T':3}
    
    for dart in dartResult:
        if dart.isdigit():
            num+=dart
        elif dart in SDT:
            tmp = int(num) ** SDT[dart]
            scorelist.append(tmp)
            num=''
        elif dart=='#':
            scorelist[-1] *= (-1)
        elif dart=='*':
            scorelist[-1] *= 2
            if len(scorelist)>=2:
                scorelist[-2] *= 2
            
    return sum(scorelist)



'''
num = ''
scorelist=[]

1. 점수인 경우
num += dart

2. SDT 인 경우
num int화 => SDT제곱 => scorelist에 넣기
=> num='' 초기화

3. *#인 경우
# : 자기자신 * -1
*: 자기자신 *2 , 이전점수 *2
'''