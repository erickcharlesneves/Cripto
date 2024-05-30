#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#TEE criptografia 

# Cifragem de mensagem especificada 


Letra = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔúÚüÜçÇ'

chave= 'ÚüÜçÇ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔú'


mensagem = 'Olá darth'
saida = ''
modo = 'cifrar'

for simbolo in mensagem:
    if simbolo in Letra:
        num = Letra.find(simbolo) # Número do símbolo
        num2 = chave.find(simbolo)
        if modo == 'cifrar':
            saida+=chave[num]
        elif modo == 'decifrar':
            saida+=Letra[num2]


    else:
        # Acrescenta símbolo sem codificação
        saida += simbolo

# Imprime na tela mensagem de saída
print(saida)


