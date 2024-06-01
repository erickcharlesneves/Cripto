#OBS: Utilizar sage math (online) ou instalar pycrypto com as bibliotecas de criptografia, Crypto. no python. Para conseguir visualizar a sa�da

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

# Solicita ao usu�rio que insira uma mensagem
MSG = input("Insira a mensagem a ser encriptada:")

# criptografa
b_MSG = bytearray(MSG, encoding="utf-8")  # mensagem deve ser um array de bytes

# AES utilizando CBC exige que os dados sejam passados em blocos cujo tamanho seja m�ltiplo de 16 bytes.
# adequando o tamanho da mensagem original para que seja multipla de block_size definido
block_size = 16
n = len(b_MSG)
spaces_add = block_size - n % block_size # calcular a qtd de espa�os vamos adicionar ao final da mensagem
new_b_MSG = bytearray(MSG + ' ' * spaces_add, encoding="utf8")


# objeto que criptografa AES com a chave gerada
aes = algorithms.AES(key)

# modo com o inicializar o vetor criado na inicializa��o
cbc = modes.CBC(iv)

# criar o cipher 
cipher = Cipher(aes, cbc, backend=backend)

# obtem o encriptador a partir do cipher
encryptor = cipher.encryptor()

# encriptar - cifra
ct = encryptor.update(new_b_MSG) + encryptor.finalize()

# obtem o decriptador - decifragem
decryptor = cipher.decryptor()

# Executar a opera��o de descriptografia e armazenar na vari�vel
decrypted_message = decryptor.update(ct) + decryptor.finalize()

# Exibindo �s etapas em msg do processo de encriptar e decriptar
print("\n""Mensagem encriptada concatenada na vari�vel ct:", ct, "\n")
print("M�todo embutido decodificar bytes de objeto em:", ct . decode, "\n")
print("Objeto criptografador:", encryptor,"\n")
print("Objeto descriptografador:", decryptor, "\n""\n")

# Exibe a mensagem descriptografada e decoding utf-8 (caracteres)
print("Mensagem inserida descriptografada:", decrypted_message . decode ('utf-8'))


