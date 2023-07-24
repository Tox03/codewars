def perimeter(n):  # сумма чисел фибоначи до n+1 элемента умноженная на 4
    temporal = [1, 1]
    n -= 1
    for i in range(n):
        temporal.append(temporal[i + 1] + temporal[i])
    return sum(temporal)*4


print(perimeter(500))