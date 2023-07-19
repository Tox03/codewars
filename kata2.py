def narcissistic(number):  #Нарцистические числа (true or false)
    number_string = str(number)
    len_number = len(number_string)
    numbers = [int(i) ** len_number for i in number_string]
    return sum(numbers) == number


print(narcissistic(4887))
