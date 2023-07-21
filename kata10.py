def make_readable(seconds):  # переводит секунды в часы, минуты и секунды
    sec = str(seconds % 60)
    min = str(seconds % 3600 // 60)
    hour = str(seconds // 3600)
    if len(sec) < 2:
        sec = "0" + sec
    if len(min) < 2:
        min = "0" + min
    if len(hour) < 2:
        hour = "0" + hour
    return f'{hour}:{min}:{sec}'