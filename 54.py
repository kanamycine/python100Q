lst = list(map(int, input().split()))
lst.sort()
res = True
for i in range(len(lst)-1):
    if lst[i] + 1 == lst[i+1]:
        res = True
    else:
        res = False
        break
print(res)

[1, 2, 4, 5, 6]
