def solution(arr, n):
    return [a + n if (i % 2 != len(arr) % 2) else a for i, a in enumerate(arr)]
