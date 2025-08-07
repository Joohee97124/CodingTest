def solution(my_string, indices):
    return ''.join([my for i,my in enumerate(my_string) if i not in indices])