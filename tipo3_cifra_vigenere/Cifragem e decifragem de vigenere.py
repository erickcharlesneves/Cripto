#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#TEE criptografia 

# Cifragem e decifragem por vigenere (Retorna o texto inserido sem espacos e em maiusculas)

import sys
    
class Cipher(object):    # Classe cipher base para as cifras classicas
 
    def format_str(self, text):          #Retorna text sem espacos e em maiusculas
        return text.replace(' ', '').upper()
 
    def shift_alphabet(self, alphabet, shift):  #Retorna alphabet com deslocamento de valor shift
        return alphabet[shift:] + alphabet[:shift]

class Vigenere(Cipher):
 
    def __init__(self):
        self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    def repeat_password(self, password, text):  #Repete a password ate o tamanho de text

        if len(password) < len(text):
            new_pass = password * int((len(text)/len(password)))
            if len(new_pass):
                new_pass += password[:len(new_pass)]
            return new_pass.upper()
        return password.upper()
 
    def encrypt(self, plaintext, password, decrypt=False):  #Cifra plaintext com a cifra de Vigenere, Decifra se decrypt for True
   
        password = self.repeat_password(password, plaintext)
        plaintext = self.format_str(plaintext)
        textout = ''
        for idx, char in enumerate(plaintext.upper()):    # indice da letra da cifra
        
            idx_key = self.plain.find(password[idx])      
            
            c_alphabet = self.shift_alphabet(self.plain, idx_key)  # gera alfabeto cifrado
 
            if decrypt:
                idx_p = c_alphabet.find(char)
                textout += self.plain[idx_p]
            else:
                idx_p = self.plain.find(char)
                textout += c_alphabet[idx_p]
 
        return textout
 
    def decrypt(self, ciphertext, password):   #Decifra ciphertext
    
        return self.encrypt(ciphertext, password, True)
 
versao = sys.version_info[0]
 
if versao == 2:
    leitura = raw_input
elif versao == 3:
    leitura = input
 
txt_in = leitura('Mensagem a cifrar: ')
password = leitura('Palavra chave: ')
 
cifra = Vigenere()
txt_cifrado = cifra.encrypt(txt_in, password)
print
print('Mensagem cifrada: {0}'.format(txt_cifrado))
print('  Mensagem plano decifrada: {0}'.format(cifra.decrypt(txt_cifrado, password)))


