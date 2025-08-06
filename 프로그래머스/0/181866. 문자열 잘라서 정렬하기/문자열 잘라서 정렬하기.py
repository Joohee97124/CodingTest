def solution(myString):
    mys = []
    my = myString.split("x")
    for m in my:
        if ''!= m:
            mys.append(m)
        
    mys.sort()
    return mys