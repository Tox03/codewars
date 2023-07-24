def next_bigger(n):  # следующее самое большое число
    str_n = str(n)
    temporal = [-1]
    temporal2 = []
    temporal3 = set()
    for i in range(1, len(str_n) + 1):
        int_num = int(str_n[-i])
        if int_num in temporal:
            temporal3.add(int_num)
            temporal3 = sorted(list(temporal3))
            print(temporal3)
            for j in range(len(temporal3)):
                if temporal3[j] > int_num:
                    temporal4 = str(temporal3[j])
                    break
            temporal2.remove(temporal4)
            return int(str_n[:-i] + temporal4 + ''.join(sorted(temporal2+[str_n[-i]])))
        else:
            temporal3.add(int_num)
            temporal2.append(str_n[-i])
            if temporal[-1] < int_num:
                for j in range(temporal[-1] + 1, int_num):
                    temporal.append(j)
    return -1