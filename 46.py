n = ''
for i in range(1, 100+1):
    n += str(i)
res = 0
for i in n:
    res += int(i)
print(res)
