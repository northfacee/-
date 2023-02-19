# 시간복잡도

# 아이디어

from typing import *
N = input()

answer = 0
def sol(N: str) -> int:
    global answer
    for i in N:
        if i == '0' or i=='1' or answer==0:
            answer += int(i)
        else:
            answer *= int(i)
    return answer
sol(N)

print(answer)
