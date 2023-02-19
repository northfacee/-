#시간복잡도

#아이디어 -> 뭔가 수학으로 풀수있지않을까하는..
from itertools import combinations

N = list(map(int, input().split()))
bowling =  list(map(int, input().split()))

answer=0
for i in combinations(bowling, 2):
    if i[0] != i[1]:
        answer +=1

print(answer)
