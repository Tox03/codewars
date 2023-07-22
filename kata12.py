MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}


def decode_morse(morse_code):  # расшифровка азбуки морзе 1
    text = ''
    temporal = ''
    temporal2 = 0
    while morse_code[0] == ' ':
        morse_code = morse_code[1:]
    while morse_code[-1] == ' ':
        morse_code = morse_code[:-1]
    for i in range(len(morse_code)):
        if morse_code[i] == ' ' and len(morse_code) - 1 > i:
            if morse_code[i+1] == ' ' and morse_code[i+2] == ' ':
                text += MORSE_CODE[temporal]
                temporal = ''
                text += ' '
                temporal2 = 2
            elif temporal2 == 0:
                text += MORSE_CODE[temporal]
                temporal = ''
            elif temporal2 != 0:
                temporal2 -= 1
        elif morse_code[i] != ' ':
            temporal += morse_code[i]
    text += MORSE_CODE[temporal]
    return text
