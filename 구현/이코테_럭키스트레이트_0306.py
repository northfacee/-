N = input()

def solution(N):
    div = len(N)//2

    first = sum([int(i) for i in N[0:div]])
    second = sum([int(j) for j in N[div::]])

    if first == second:
        print('LUCKY')
    else:
        print('READY')
    
solution(N)
