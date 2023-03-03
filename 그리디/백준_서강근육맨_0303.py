N = int(input())
weight = list(map(int, input().split()))
answer = 0
def solution(N, weight):
    global answer
    weight = sorted(weight)

    if len(weight) % 2 == 1: #홀수
        for i in range(len(weight)//2):
            sum_w = weight[i] + weight[-i-2]
            if answer < sum_w:
                answer = sum_w
    else: #짝수
        for i in range(len(weight)//2):
            sum_w = weight[i] + weight[-i-1]
            if answer < sum_w:
                answer = sum_w
    return answer



solution(N,weight)
print(answer)
