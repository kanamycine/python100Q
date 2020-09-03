# merge sort
# 1. 리스트의 길이가 0 또는 1이면 이미 정렬 된 것으로 본다. 그렇지 않은 경우에는
# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분의 리스트로 나눈다.
# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

def merge(lst):
    lenlst = len(lst)
    if lenlst <= 1:
        return lst

    mid = lenlst // 2
    group1 = merge(lst[:mid])
    group2 = merge(lst[mid:])
    result = []

    while group1 and group2:
        if group1[0] < group2[0]:
            result.append(group1.pop(0))

        else:
            result.append(group2.pop(0))

    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))

    return result


lst = input().split(' ')
lst = [int(i) for i in lst]

print(merge(lst))
