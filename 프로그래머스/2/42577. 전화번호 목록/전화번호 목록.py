def solution(phone_book):
    hashmap = {pb:True for pb in phone_book}
    
    for pb in phone_book:
        prefix=''
        for n in pb:
            prefix += n
            if prefix in hashmap and prefix!=pb:
                return False
    
    return True