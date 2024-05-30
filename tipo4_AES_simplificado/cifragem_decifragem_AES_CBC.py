#OBS: Utilizar sage math (online) ou instalar pycrypto com as bibliotecas de criptografia, Crypto. no python. Para conseguir visualizar a saída

#TEE criptografia 

# Cifragem e decifragem AES CBC

# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

key = os.urandom(32)
key

# inicializar o vetor 
iv = os.urandom(16)
iv

MSG = "encriptar e decriptar esta mensagem"

# criptografa
b_MSG = bytearray(MSG, encoding="ascii")  # mensagem tem que ser byte array

# AES utilizando CBC exige que os dados sejam passados em blocos cujo tamanho seja múltiplo de 16 bytes.
# adequando o tamanho da mensagem original para que seja multipla de block_size definido
block_size = 16
n = len(b_MSG)
spaces_add = block_size - n % block_size # calcular a qtd de espaços vamos adicionar ao final da mensagem
new_b_MSG = bytearray(MSG + ' ' * spaces_add, encoding="utf8")


# objeto que criptografa AES com a chave gerada
aes = algorithms.AES(key)

# modo com o inicializar o vetor criado na inicialização
cbc = modes.CBC(iv)

# criar o cipher 
cipher = Cipher(aes, cbc, backend=backend)

# obtem o encriptador a partir do cipher
encryptor = cipher.encryptor()

# encriptar - cifra
ct = encryptor.update(new_b_MSG) + encryptor.finalize()

# obtem o decriptador - decifragem
decryptor = cipher.decryptor()

# decripta - decifra a mensagem para a forma original definida em MSG
decryptor.update(ct) + decryptor.finalize()


