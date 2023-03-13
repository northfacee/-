n = int(input())
houses = list(map(int, input().split()))

houses.sort()

mid = (n-1)//2 #여러개일때 가장 작은값이기 때문에
print(houses[mid])
