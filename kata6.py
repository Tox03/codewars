def solution(n):  # перевод в римские цифры (до 3999 включительно)
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    rom_num = ''
    for i in range(len(numbers)):
        if n - numbers[i] > 0:
            n -= numbers[i]
            rom_num += rom_numbers[i]
            if n - numbers[i] > 0:
                n -= numbers[i]
                rom_num += rom_numbers[i]
                if n - numbers[i] > 0:
                    n -= numbers[i]
                    rom_num += rom_numbers[i]
        if n - numbers[i] == 0:
            n -= numbers[i]
            rom_num += rom_numbers[i]
            return rom_num


print(solution(984))