#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#TEE criptografia 

# Cifragem aleatória de mensagem (baseado em cesar) especificada (de acordo com a regua)
from random import randint

regua_caracteres = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔúÚüÜçÇ'

cifrado_definido= '';
cifrado_aleat = '';

regua_caracteres_aux = list(regua_caracteres);

n = len(regua_caracteres);
for i in range(0,n):
    ind = randint(0,len(regua_caracteres_aux)-1);
    cifrado_aleat += regua_caracteres_aux.pop(ind);

mensagem = 'Olá darth'
K = 7
modo = 'cifrar'

# Cifragem da mensagem, símbolo a símbolo
for simbolo in mensagem:
    if simbolo in regua_caracteres:
        num = regua_caracteres.find(simbolo) # Número do símbolo
        if modo == 'cifrar':
            num += K
        elif modo == 'cifrar':
            num -= K
        num = num % len(regua_caracteres)

        # Acrescenta símbolo cifrado na mensagem 
        cifrado_definido += regua_caracteres[num]

  
print("\nRegua dos caracteres: ", regua_caracteres)
print("\nPermutação aleatória:\n", cifrado_aleat)
print("\nPermutação definida da mensagem:\n ", cifrado_definido) 
