n = input()
cnt = 0
for i in n:
    if i == ' ':
        cnt += 1

print(cnt+1)

# 모범답
n = input()
l = list(n.strip().split())
print(len(l))
