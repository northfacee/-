n = input()
stack = []
for i in n:
    if i == '(':
        stack.append('(')
    else:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
print(len(stack))
