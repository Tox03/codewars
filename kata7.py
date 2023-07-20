def solution(s):  # разбивает текст по заглавным буквам
    temporal = ''
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            temporal += f' {i}'
        else:
            temporal += i
    return temporal


print(solution('camelCasing'))