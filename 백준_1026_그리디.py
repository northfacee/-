n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A=sorted(a)
B=sorted(b, reverse=True)

plus=0
for i in range(n):
    plus += (A[i]*B[i])
print(plus)
