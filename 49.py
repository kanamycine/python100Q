lst = list(map(int, input().split()))
maxvalue = 0
maxvalue = lst[0]
for i in range(len(lst)):
    if lst[i] > maxvalue:
        maxvalue = lst[i]
print(maxvalue)
