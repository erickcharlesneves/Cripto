# -*- coding: utf-8 -*-
"""
Created on Fri May 30 00:03:32 2024

@author: erick
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encriptar_aes(texto_plano, chave):
    # Gera um vetor de inicialização aleatório
    iv = get_random_bytes(16)
    # Cria o objeto de cifragem AES no modo CBC
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    # Pad (preencher) o texto plano para que seja múltiplo de 16 bytes
    texto_plano_preenchido = pad(texto_plano.encode('utf-8'), AES.block_size)
    # Encripta o texto plano preenchido
    texto_cifrado = cifra.encrypt(texto_plano_preenchido)
    # Retorna o vetor de inicialização e o texto cifrado concatenados
    return iv + texto_cifrado

def decriptar_aes(texto_cifrado, chave):
    # Extrai o vetor de inicialização do início do texto cifrado
    iv = texto_cifrado[:16]
    # Extrai o texto cifrado real
    texto_cifrado = texto_cifrado[16:]
    # Cria o objeto de cifragem AES no modo CBC com o vetor de inicialização extraído
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    # Decripta o texto cifrado
    texto_plano_preenchido = cifra.decrypt(texto_cifrado)
    # Remove o preenchimento (pad)
    texto_plano = unpad(texto_plano_preenchido, AES.block_size)
    # Retorna o texto plano
    return texto_plano.decode('utf-8')

# Executando teste
chave = get_random_bytes(16)  # AES-128 usa uma chave de 16 bytes
texto_plano = "Texto a ser encriptado"

texto_cifrado = encriptar_aes(texto_plano, chave)
print(f"Texto cifrado: {texto_cifrado}")

texto_decifrado = decriptar_aes(texto_cifrado, chave)
print(f"Texto decifrado: {texto_decifrado}")