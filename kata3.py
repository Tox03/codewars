def duplicate_count(text):  # сколько букв повторяется в слове
    text = text.lower()
    text = sorted(text)
    number_of_duplicates_letters = 0
    if len(text) == 0:
        return 0
    if text[0] == text[1]:
        number_of_duplicates_letters += 1
    for i in range(1, len(text) - 1):
        if text[i] == text[i + 1] and text[i] != text[i - 1]:
            number_of_duplicates_letters += 1
    return number_of_duplicates_letters


print(duplicate_count('abcdeaa'))
