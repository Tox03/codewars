def rot13(message):  # шифр цезаря (перенос на 13 символов вперёд)
    new_message = ''
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    big_alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(message)):
        if message[i] in alfabet:
            new_message += alfabet[(alfabet.index(message[i]) + 13) % 26]
        elif message[i] in big_alfabet:
            new_message += big_alfabet[(big_alfabet.index(message[i]) + 13) % 26]
        else:
            new_message += message[i]
    return new_message


print(rot13('test'))