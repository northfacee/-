import re
n = input()
g=re.split('([-|+|*])',n)
for i in range(len(g)):
     g[i] =g[i].lstrip('0')
a =''.join(g)
a=a.split('-')
    
plus = 0
for i in range(0, len(a)):
    if (str(a[i][-1]) == '+'):
        a[i][-1]=a[i][-1].replace('+','').replace('-','')
    if (str(a[i][-1]) == '-'):
        a[i][-1]=a[i][-1].replace('+','').replace('-','')
        
    if i == 0:
        plus += eval(a[i])
    else:
        plus -= eval(a[i])
print(plus)
