# -*- coding: utf-8 -*-
"""
Created on Thu May 30 02:03:34 2024

@author: erick

"""
#TEE criptografia 

# Cifra de hill (sem necessidade de definir matriz de frase a ser criptografada do criptograma, e nem mapeamento(dicionario))

import numpy as np

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔúÚüÜçÇ0123456789 .,!?@#$%^&*()-_=+[]{}|;:\'",<>/~`' #incluindo caracteres
matriz_chave = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Matriz chave de 3x3

def frase_para_numeros(frase, alfabeto):
    # Convertendo a frase para uma lista de números com base no alfabeto
    return [alfabeto.index(c) for c in frase]

def numeros_para_frase(numeros, alfabeto):
    # Convertendo uma lista de números de volta para frase
    return ''.join(alfabeto[num] for num in numeros)

def preencher_frase(frase, tamanho_bloco, alfabeto):
    # Preenchendo a frase para garantir que seu comprimento seja múltiplo do tamanho do bloco
    while len(frase) % tamanho_bloco != 0:
        frase += alfabeto[-1]  # Usando o último caractere do alfabeto como preenchimento
    return frase

def inverso_modular(a, m):
    # Calculando o inverso modular de 'a' módulo 'm'
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def inversa_matriz_modular(matriz, modulo):
    # Calculando a inversa modular de uma matriz
    det = int(round(np.linalg.det(matriz)))
    det_inv = inverso_modular(det, modulo)
    adj = np.round(det * np.linalg.inv(matriz)).astype(int)
    matriz_inv = (det_inv * adj) % modulo
    return matriz_inv

def cifra_hill(frase_plano, matriz_chave, alfabeto):
    tamanho_bloco = matriz_chave.shape[0]
    frase_plano = preencher_frase(frase_plano, tamanho_bloco, alfabeto)
    numeros_frase_plano = frase_para_numeros(frase_plano, alfabeto)
    numeros_cifrados = []

    for i in range(0, len(numeros_frase_plano), tamanho_bloco):
        bloco = np.array(numeros_frase_plano[i:i+tamanho_bloco])
        bloco_cifrado = np.dot(matriz_chave, bloco) % len(alfabeto)
        numeros_cifrados.extend(bloco_cifrado)

    return numeros_para_frase(numeros_cifrados, alfabeto)

def decifra_hill(frase_cifrado, matriz_chave, alfabeto):
    tamanho_bloco = matriz_chave.shape[0]
    numeros_frase_cifrado = frase_para_numeros(frase_cifrado, alfabeto)
    numeros_decifrados = []

    matriz_chave_inv = inversa_matriz_modular(matriz_chave, len(alfabeto))

    for i in range(0, len(numeros_frase_cifrado), tamanho_bloco):
        bloco = np.array(numeros_frase_cifrado[i:i+tamanho_bloco])
        bloco_decifrado = np.dot(matriz_chave_inv, bloco) % len(alfabeto)
        numeros_decifrados.extend(bloco_decifrado)

    return numeros_para_frase(numeros_decifrados, alfabeto).rstrip(alfabeto[-1])  # Remover o preenchimento

# Executando

frase_plano = "Olá, Bob! Cyberpunk20777"
frase_cifrado = cifra_hill(frase_plano, matriz_chave, alfabeto)
frase_decifrado = decifra_hill(frase_cifrado, matriz_chave, alfabeto)

print(f"frase original: {frase_plano}")
print(f"frase cifrada: {frase_cifrado}")
print(f"frase decifrada: {frase_decifrado}")