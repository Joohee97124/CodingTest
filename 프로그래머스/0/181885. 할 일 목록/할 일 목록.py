def solution(todo_list, finished):
    return [todo_list[i] for i,finish in enumerate(finished) if finish==False]