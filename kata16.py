from math import sqrt


def prime(n):
    for i in range(2, int(sqrt(n))):
        print(i)
        if n % i == 0:
            return False
    return True


print(prime(6))
