# 시간복잡도 -> 1초, max(N) = 1000
# 2백만???

# 아이디어 -> eval?, for문으로 처음에 숫자를 받고, 그다음 for문으로 len을 받아 sum(coin)? 

from typing import *

N = int(input())
coins = list(map(int, input().split()))

answer =0
num = []

def sol(coins: List) -> int:
    global num, answer
    coins.sort()
    for i in range(len(coins)): # 1000
        for j in range(len(coins)): # 1000

            if sum(coins[i:i+j]) in num:
                continue
            else:
                num.append(sum(coins[i:i+j]))
    
    for miss in range(max(num)): #1,000,000
        if miss not in num:
            answer += miss
            break

sol(coins)
print(answer)
