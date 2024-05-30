# -*- coding: utf-8 -*-
"""

@author: erick

"""
#TEE criptografia 

# Cifra de hill (limitado)

import numpy
from pprint import pprint

# Mapeando letras para números
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12
n = 13
o = 14
p = 15
q = 16
r = 17
s = 18
t = 19
u = 20
v = 21
x = 22
w = 23
y = 24
z = 25

chave = numpy.matrix ([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

cryptogram = "olabobboy"
frase = numpy.matrix ([[o, l, a], [b, o, b], [b, o, y]])
frase_encr = frase*chave
frase_encriptar = frase_encr%26

print("\nCriptograma de acordo com a nossa matriz e caracteres substituidos por números de acordo com tabela e seguimentado na matriz abaixo: ")
pprint(frase_encriptar)

chave_inv = numpy.matrix ([[4, 9, 15], [15, 17, 6], [24, 0, 17]])
frase_des = frase_encriptar*chave_inv
frase_desencriptar = frase_des%26

print("\nDescriptografia de acordo com a nossa matriz e caracteres substituidos por números de acordo com tabela e seguimentado na matriz abaixo: ")
pprint(frase_desencriptar)

# Transformamos a matriz em uma lista unidimensional
list_calculated_cryptogram = frase_desencriptar.flatten().astype(numpy.int64)

print("\nLista unidimensinal dos valores calculados:")
pprint(list_calculated_cryptogram)

print("\nA partir da lista unidimensinal podemos fazer a conversão de decimal para caracteres, usando um loop de comparação com a nossa tabela de caracteres, para conferir o resultado basta comparar os valores da matriz de descriptografia com a nossa tabela de caracteres definida, em cima no código")