def tabela_vigenere():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    return alfabeto


def enc_vig(txtin=''):
    alfabeto = tabela_vigenere()
    key = input("Informe a chave: ")
    key = key.strip()
    key = key.replace(" ", "")
    key = key.lower()
    saida = ""

    kpos = []  # return the index of characters ex: if k='d' then kpos= 3
    for x in key:
        kpos.append(alfabeto.find(x))
    i = 0

    for x in txtin:
        if x == ' ':
            saida += ' '
        else:
            if i == len(kpos):
                i = 0
            pos = alfabeto.find(x.lower()) + kpos[i]  # find the number or index of the character and perform the shift with the key
            if pos > 25:
                pos = pos - 26  # check you exceed the limit
            saida += alfabeto[pos].capitalize()  # because the cipher text always capital letters
            i += 1
    return saida


def dec_vig(txtin=''):

    key = input("Informe a chave: ")
    key = key.strip()
    key = key.replace(" ", "")
    key = key.lower()
    alfabeto = tabela_vigenere()
    saida = ""
    kpos = []

    for x in key:
        kpos.append(alfabeto.find(x))

    i = 0
    for x in txtin:
        if x == ' ':
            saida += ' '
        else:
            if i == len(kpos):
                i = 0
            pos = alfabeto.find(x.lower()) - kpos[i]
            if pos < 0:
                pos = pos + 26
            saida += alfabeto[pos].lower()
            i += 1
    return saida