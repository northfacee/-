k = int(input())
test = [input() for i in range(k)]

for case in test:
    stack = []
    for i in case:
        if i == '(':
            stack.append('(')
        else:
            if len(stack)==0:
                stack.append(')')
            elif stack[-1] == '(':
                stack.pop()
    if len(stack)==0:
        print('YES')
    else:
        print('NO')
