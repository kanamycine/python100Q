# quick sort

def quick(lst):
    lenlst = len(lst)
    if lenlst <= 1:
        return lst

    standard = lst.pop(lenlst//2)
    group1 = []
    group2 = []

    for i in range(lst-1):
        if lst[i] < standard:
            group1.append(lst[i])
        else:
            group2.append(lst[i])
    return quick(group1) + [standard] + quick(group2)


lst = input().split(' ')
lst = [int(i) for i in lst]

print(quick(lst))
