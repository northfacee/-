n, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

count =1
def solution(positions, l):
    global count
    start = positions[0]
    end = start + l # 

    for i in range(n):
        if positions[i] < end:
            continue
        else:
            start = positions[i]
            end = start + l
            count += 1

solution(positions, l)
print(count)
