#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt


def base64_table(index=None):
    tabela = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"
    ]

    if index:
        return tabela[index]
    else:
        return tabela


def encrypt(txtin, formato='d', salto=None):

    output = ''

    if txtin == '':
        return False
    else:
        if formato == 'h':
            for c in txtin:
                output += str(hex(ord(c)))
        elif formato == 'o':
            for c in txtin:
                output += str(oct(ord(c)))
        elif formato == 'b':
            output = enc_base64(txtin)
        elif formato == 'c':
            shift = salto
            if int(salto) == 0:
                output = shift_cesar('e', txtin)
            else:
                output = enc_cesar(txtin, shift)
        elif formato == 'v':
            output = enc_vig(txtin)
        else:
            for c in txtin:
                output += str(ord(c))

        return output


def decrypt(txtin, formato='d', salto=None):

    output = ''

    if txtin == '':
        return False
    else:
        if formato == 'h':
            for hexa in txtin[:: 2]:
                output += chr(int(hexa, 16))
        elif formato == 'o':
            for octal in txtin[:: 3]:
                output += chr(int(octal, 8))
        elif formato == 'b':
            output = dec_base64(txtin)
        elif formato == 'c':
            shift = salto
            if int(salto) == 0:
                output = shift_cesar('d', txtin)
            else:
                output = dec_cesar(txtin, shift)
        elif formato == 'v':
            output = dec_vig(txtin)
        else:
            aux = ''
            for decimal in txtin:
                aux += str(decimal)
                if 65 <= int(aux) <= 125:
                    output += chr(int(aux))
                    aux = ''

        return output


def enc_cesar(txtin= '', salto=1):

    saida = ''

    if txtin != '':
        entrada = txtin.upper()
        for c in entrada:
            if c == ' ':
                saida += ' '
            else:
                new_c = ord(c)
                for i in range(1, int(salto) + 1, 1):
                    new_c += 1
                    if new_c > 90:
                        new_c = 65
                saida += chr(new_c)
    return saida


def dec_cesar(txtin='', salto=1):

    saida = ''

    if txtin != '':
        entrada = txtin.upper()
        for c in entrada:
            if c == ' ':
                saida += ' '
            else:
                new_c = ord(c)
                for i in range(1, int(salto) + 1, 1):
                    new_c -= 1
                    if new_c < 65:
                        new_c = 90
                saida += chr(new_c)
    return saida


def shift_cesar(type='', txtin = ''):

    saidas = []

    for i in range(1, 26, 1):
        if type == 'e':
            saidas.append(enc_cesar(txtin, i))
        if type == 'd':
            saidas.append(dec_cesar(txtin, i))

    saida = ''
    for i, v in enumerate(saidas):
        saida += str(i+1) + " - " + v + "\n"

    return saida


def tabela_vigenere():

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    return alfabeto


def enc_vig(txtin=''):

    alfabeto = tabela_vigenere()
    key = raw_input("Informe a chave: ")
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

    key = raw_input("Informe a chave: ")
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


def enc_base64(txtin=''):

    bin_string = ''
    for c in txtin:
        # convert char to int
        inteiro = ord(c)

        # convert int to bin
        binario = bin(inteiro)

        # agrupa bin
        bin_string += str(binario).replace("0b", '0')

    # divide em grupos de 3 bytes
    controle = 0
    blocos = []
    bin_bloco = ''
    for i,v in enumerate(bin_string):
        bin_bloco += str(v)
        controle += 1
        if controle == 24 or i == len(bin_string) - 1:
            blocos.append(str(bin_bloco))
            bin_bloco = ''
            controle = 0

    if len(blocos[-1]) % 24 != 0:
        blocos[-1] += "0" * (24 - (len(blocos[-1]) % 24))

    # separar cada grupo em grupos de 6 bits
    grupo6_bits = []

    for grupo in blocos:
        for i in range(0, len(grupo) - 1, 6):
            grupo6_bits.append(grupo[i:i+6])

    # converter binario > int > ascii
    output = ''
    for b in grupo6_bits:
        decimal = int(b, 2)
        if decimal == 0:
            output += "="
        else:
            output += base64_table(decimal)

    return output


def dec_base64(txtin = ''):

    tabela = base64_table()

    txtin_chars = []
    for c in txtin:
        if c == '=':
            txtin_chars.append(0)
        else:
            txtin_chars.append(tabela.index(c))

    bins = []
    for indice, value in enumerate(txtin_chars):
        bins.append(str(bin(value)).replace("0b", "").zfill(6))

    grupos_3bytes = []
    aux = ''
    controle = 0
    for b in bins:
        aux += str(b)
        controle += 1
        if controle == 4:
            grupos_3bytes.append(aux)
            aux = ''
            controle = 0


    bytes_ind = []
    for grupo in grupos_3bytes:
        bytes_ind.append(grupo[0:8])
        bytes_ind.append(grupo[8:16])
        bytes_ind.append(grupo[16:24])

    output = ''
    for bi in bytes_ind:
        code = int(bi,2)
        if code != 0:
            output += chr(code)

    return output


def main(argv):

    tipo = 'e'
    formato = 'd'
    salto = 1
    opts = []
    args = []

    try:
        opts, args = getopt.getopt(argv, "hedf:s:", ["help", "encrypt", "decrypt", "format=", "salto=", "key="])
    except getopt.GetoptError:
        print('criptodecripto.py -[e|d] -f <format> text')
    for opt, arg in opts:
        if opt in('-h', '--help'):
            print('criptodecripto.py -[e|d] -f <format> text \n <format> : h|d|o|b|c')
            sys.exit()
        elif opt in ("-d", "--decrypt"):
            tipo = "d"
        elif opt in ("-e", "--encrypt"):
            tipo = "e"
        elif opt in("-f", "--format"):
            formato = arg[0]
        elif opt in("-s", '--salto'):
            salto = arg[0]
        else:
            assert False, "operação não suportada"

    if formato not in ('h', 'o', 'd', 'b', 'c', 'v'):
        print("Formato inválido, utilize h (hexadecimal), o (octal), d (decimal), b (base64), c (cifra de cesar) ou v (vigenere)")
    else:
        if tipo == 'd':
            retorno = decrypt(args[0], formato, salto)
            if retorno:
                print(retorno)
        else:
            retorno = encrypt(args[0], formato, salto)
            if retorno:
                print(retorno)
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
