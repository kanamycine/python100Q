lst = list(map(str, input().split()))
count = 0
for i in range(len(lst)):
    if lst.count(lst[i-1]) < lst.count(lst[i]):
        count = i - 1
print(i)
