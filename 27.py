# 내답안
# a, b = map(str, input().split())
# d, c = map(int, input().split())

# student = {a: c, b: d}
# print(student)

# 모범답안

keys = input().split()
print(keys)
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)


## dict ? zip ? 