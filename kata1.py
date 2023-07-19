def solution(number):  # сумма всех натуральных чисел, которые делятся на 3 или 5
    # и меньше введённого числа (число в сумме учитывается только один раз), для 10 это сумма равняется 23
    sum_all = 0
    if number > 0:
        number = number - 1
        number_of_three = number // 3
        number_of_five = number // 5
        sum_of_three = (2 * 3 + 3 * (number_of_three - 1)) * number_of_three / 2
        sum_of_five = (2 * 5 + 5 * (number_of_five - 1)) * number_of_five / 2
        sum_all = sum_of_three + sum_of_five - ((2 * 15 + 15 * (number // 15 - 1)) * (number // 15) / 2)
    return sum_all


print(solution(22))
