def solution(myString, pat):
    for my in range(len(myString), -1, -1):
        if pat == myString[my-len(pat):my]:
            return myString[:my]
        