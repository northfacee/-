n = input()

count=0
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        count +=1
if count==1:
    print(count)
elif count%2 ==1:
    print(count//2+1)
else:
    print(count//2)
