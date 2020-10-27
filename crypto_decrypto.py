#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from cesar_cipher import dec_cesar, enc_cesar, shift_cesar
from base64_cipher import dec_base64, enc_base64
from vigenere_cipher import enc_vig, dec_vig


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
            print('criptodecripto.py -[e|d] -f <format> text \n <format> : h|d|o|b|c|v')
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
