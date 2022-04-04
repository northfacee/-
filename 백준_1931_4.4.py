
n = int(input())
rooms = [list(map(int,input().split())) for i in range(n)]
room = sorted(rooms,key=lambda x :(x[1],x[0]))

count = 0
time = 0


for start, end in room:
    if start >= time and end >= time:
        time = end
        count +=1
    
        
print(count)
