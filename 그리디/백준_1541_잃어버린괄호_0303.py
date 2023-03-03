N = input()
answer = 0

def solution(N):
    global answer
    num = N.split('-')
    
    if len(num) == 1:
        answer += eval(num[0])

    else: # - 부호가 있을

        for i in range(len(num)):
            w = num[i].split('+')
            if i == 0:
                for m in w:
                    answer += int(m)
            else:
                for j in w:
                    answer -= int(j)


solution(N)
print(answer)
