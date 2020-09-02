score = list(map(int, input().split()))
score.sort()
count = 3
for i in range(len(score)-1, 0, -1):
    if score[-3] == score[i]:
        count += 1
print(count)
