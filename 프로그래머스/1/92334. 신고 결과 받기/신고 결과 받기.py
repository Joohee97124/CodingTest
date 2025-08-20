def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ids = {i:0 for i in id_list}
    people = {i:set() for i in id_list}
    
    for re in report:
        a,b = re.split(" ")
        if b not in people[a]:
            people[a].add(b)
            ids[b] += 1
    
    answer_dict = {name: 0 for name in id_list}
    for key,value in ids.items():
        if value >= k:
            for pe,wh in people.items():
                if key in wh:
                    answer_dict[pe] += 1
                    
    answer = [answer_dict[i] for i in id_list]        
    return answer

'''
1. id_list 를 돌면서 dict을 2개 만든다
- (1) 신고 받은 누적수 ID:0
- (2) ID가 신고한 사람 ID:[,] 형태로  
2. report를 돌면서 
- (2) key값이 같으면 report의 value 값을 set()형태로 ID:{,,} 에 넣어줌
3.  (2)의 리스트 길이만큼 key값이 같은 애한테 (1)을 만들어줌
4. id_list 크기만큼의 []리스트를 0으로 만들고,
(1) 신고받은 누적수 를 돌면서 k보다 value값이 같거나 크면
(2) value 값에 신고받은 누적수의 key값이 있는 index 값을 찾아서
id_list크기만큼 만든 리스트에 +=1 해줌


'''