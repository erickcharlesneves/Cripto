# -*- coding: utf-8 -*-
"""

@author: erick

"""
#TEE criptografia 

# Cifra de hill e decifra

import numpy as np #para operações com matriz
from pprint import pprint

# Mapeamento das letras para números
letter_to_num = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
    'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
    'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

# Criando o mapeamento reverso de números para letras (dicionário)
num_to_letter = {v: k for k, v in letter_to_num.items()}

# Matriz de chave para criptografia
chave = np.matrix([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

# Criptograma e frase a ser criptografada
cryptogram = "olabobboy"
frase = np.matrix([[letter_to_num['o'], letter_to_num['l'], letter_to_num['a']], 
                   [letter_to_num['b'], letter_to_num['o'], letter_to_num['b']], 
                   [letter_to_num['b'], letter_to_num['o'], letter_to_num['y']]])

# Criptografia
frase_encr = frase * chave
frase_encriptar = frase_encr % 26

print("\nCriptograma de acordo com a nossa matriz e caracteres substituídos por números de acordo com a tabela e segmentado na matriz abaixo: ")
pprint(frase_encriptar)

# Matriz de chave inversa para descriptografia
chave_inv = np.matrix([[4, 9, 15], [15, 17, 6], [24, 0, 17]])
frase_des = frase_encriptar * chave_inv
frase_desencriptar = frase_des % 26 #Multiplica a matriz da mensagem pela matriz da chave e aplicamos o módulo 26 para obter a matriz criptografada

print("\nDescriptografia de acordo com a nossa matriz e caracteres substituídos por números de acordo com a tabela e segmentado na matriz abaixo: ")
pprint(frase_desencriptar)

# Transformação da matriz em uma lista unidimensional
list_calculated_cryptogram = np.array(frase_desencriptar).flatten().astype(int)

print("\nLista unidimensional dos valores calculados:")
pprint(list_calculated_cryptogram)

# Conversão da lista de números para caracteres (Itera sobre a lista unidimensional e substituímos cada número pelo caractere correspondente usando o dicionário num_to_letter.)
decoded_frase = ''.join(num_to_letter[num] for num in list_calculated_cryptogram)

print("\nFrase descriptografada:")
print(decoded_frase)