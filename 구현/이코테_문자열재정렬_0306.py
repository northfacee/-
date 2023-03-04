from typing import *

N = input()

def solution(N : str) -> str:
    count = 0
    for i in N:
        if i.isdigit():
            count +=1

    N = sorted(N, key=lambda x : str(x))
    alpha = ''.join(N[count::])
    num = str(sum([int(i) for i in N[:count]]))
    return print(alpha+num)

solution(N)
