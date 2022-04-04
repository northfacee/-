n = int(input())
block = list(map(int, input().split()))
count = int(input())

first = 0
last = len(block)-1
blocked = sorted(block)

for i in range(1,count+1):
    blocked[last] -= 1
    blocked[first] += 1
    count -= 1
    blocked = sorted(blocked)
    if i ==50:
        print(blocked[last] - blocked[first])
        
