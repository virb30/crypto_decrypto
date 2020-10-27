LAST_VALID_ASCII = 90
FIRST_VALID_ASCII = 65

def enc_cesar(text_in='', salt=1):
    output = []
    if text_in == '':
        return ''.join(output)

    decimal_text = [ord(text.upper()) for text in text_in]
    for c in decimal_text:
        if c not in range(FIRST_VALID_ASCII, LAST_VALID_ASCII + 1):
            output.append(c)
        for i in range(1, int(salt) + 1, 1):
            c = (c + 1) if (c + 1) <= LAST_VALID_ASCII else FIRST_VALID_ASCII
        output.append(c)
    return ''.join(chr(char) for char in output)


def dec_cesar(text_in='', salt=1):
    output = []
    if text_in == '':
        return ''.join(output)

    decimal_text = [ord(text.upper()) for text in text_in]
    for c in decimal_text:
        if c not in range(FIRST_VALID_ASCII, LAST_VALID_ASCII + 1):
            output.append(c)
        for i in range(1, int(salt) + 1, 1):
            c = (c - 1) if (c - 1) >= FIRST_VALID_ASCII else LAST_VALID_ASCII
        output.append(c)
    return ''.join(chr(char) for char in output)


def shift_cesar(type='d', text_in=''):
    outputs = []

    for i in range(1, 26, 1):
        if type == 'e':
            outputs.append((enc_cesar(text_in, i), i))
        if type == 'd':
            outputs.append((dec_cesar(text_in, i), i))

    return '\n'.join(f'{i} - {output}' for output, i in outputs)