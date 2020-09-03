n = int(input())


def prime(n):
    if n != 1:
        for f in range(2, n):
            if n % f == 0:
                return False
    else:
        return False

    return True


print(prime(n))
