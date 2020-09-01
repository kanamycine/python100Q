string = input()
result = []
for i in string:
    if ord(i) < 97:
        result.append(i)
print(result)
