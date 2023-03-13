T = int(input())

for _ in range(T):
    N = int(input())
    applicants = sorted([list(map(int, input().split())) for _ in range(N)])
    count = 1
    w = applicants[0][1]

    for _,score in applicants[1:]:
        #print(score)
        if score < w:
            count +=1
            w = score
    print(count)
