N = int(input())

dates = [list(map(int, input().split())) for _ in range(N)]
dates = sorted(dates, key=lambda x : (x[0],-x[1]))
#dates = dates.sort(key=lambda x : (x[0],-x[1])) 이땐 정렬이 안됨;;

answer = 0
def solution(dates):
    global answer

    max_date = max(max(d) for d in dates)
    calender = [0] * (max_date+1)

    for s,l in dates:
        for cnt in range(s,l+1):
            calender[cnt] +=1

    col = 0
    row = 0

    for k in range(len(calender)):

        if calender[k] !=0:
            col = max(calender[k], col)
            row +=1
        else:
            answer += col * row
            col, row =0,0
    answer += row * col

    return answer

solution(dates)
print(answer)
