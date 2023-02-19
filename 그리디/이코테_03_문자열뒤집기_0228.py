# 시간복잡도

# 아이디어 -> 연속된 split 이 같으면 상관없음, 더 적은쪽을 바꿔준다.

N = input()
count =0

def sol(N: str) -> int:
    global count
    one = N.count('1')
    zero = N.count('0')

    for i in range(len(N)-1):
        #print(N[i])
        if one >= zero: #1로 바꿈
            if N[i] == N[i+1]:
                continue
            else:
                if N[i] == '0':
                    count +=1

        else: # one < zero, 0으로 바꿈
            if N[i] ==N[i+1]:
                continue
            else:
                if N[i] == '1':
                    count +=1
    return count

sol(N)
print(count)
