def find_nb(m):  # найти n из суммы кубов (дана сумма кубов 1^3 + 2^3 + 3^3 + n^3, нужно найти n)
    temporal = 0
    while m > 0:
        temporal += 1
        m -= temporal * temporal * temporal
    if m < 0:
        return -1
    else:
        return temporal