total = 0
count = 0
limit = int(input())
n = int(input())

for i in range(n):
    if total <= limit:
        total += int(input())
        count = i
print(count)
