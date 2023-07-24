def strip_comments(string, markers):  # Удаляет из строки все символы, стоящие дальше чем любой элемент из markers
    if len(markers) == 0:
        return string
    marker = markers[0]
    for i in markers:
        string = string.replace(i, marker)
    string_with_no_new_strings = str(string).split('\n')
    temporal = ''
    for i in string_with_no_new_strings:
        if i == ' \n':
            temporal += '\n'
            continue
        position = i.find(marker)
        if position != -1:
            temporal += i[:position] + '\n'
            if len(temporal) > 1:
                while temporal[-2] == ' ':
                    temporal = temporal.replace(' \n', '\n')
                    if len(temporal) == 1:
                        break
            if len(temporal) > 1:
                while temporal[-2] == '\t':
                    temporal = temporal.replace('\t', '')
                    if len(temporal) == 1:
                        break
        else:
            temporal += i + '\n'
    return temporal[:-1]

print(strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd')