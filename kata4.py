def get_count(sentence):  # подсчёт английских гласных (a, e, i, o, u)
    return sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')


print(get_count('aeiou'))