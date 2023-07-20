def printer_error(s):  # подсчёт букв больше m в слове
    return f'{sum([1 for i in s if i in "nopqrstuvwxyz"])}/{len(s)}'


print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))