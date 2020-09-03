n = input()

stack = []

for i in n:
    stack.append(i)
res = True
while stack:
    if stack.pop(0) == '(':
        if stack.pop(0) == ')':
            res = True
        else:
            res = False
    else:
        res = False

print(res)
