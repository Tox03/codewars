from math import sqrt


def list_squared(m, n):  # Находит числа из диапозона, которые соостветствуют условию: сумма квадратов делителей
    # является квадратом числа
    temporal2 = []
    for i in range(m, n + 1):
        temporal = []
        if i < 1000:
            for j in range(1, i + 1):
                if i % j == 0:
                    temporal.append(j)
            summa = 0
            for j in temporal:
                summa += j * j
        else:
            for j in range(1, int(sqrt(i))):
                if i % j == 0:
                    temporal.append(j)
                    temporal.append(i // j)
            summa = 0
            for j in temporal:
                summa += j * j
        if int(sqrt(summa)) == sqrt(summa) and summa != 1 and summa != 0:
            temporal2.append([i, summa])
    if m == 1:
        return [[1, 1]] + temporal2
    else:
        return temporal2


print(list_squared(1, 1000000))
