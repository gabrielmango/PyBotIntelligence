import os
import random

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae')
textos_boas_vindas_respostas = ('hey', 'olá', 'opa', 'oi', 'bem-vindo', 'como você está?')

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return random.choice(textos_boas_vindas_respostas) 




if __name__ == '__main__':
    os.system('cls')

    mensagem_teste = 'olá tudo bem'
    print(mensagem_teste.split())

    responder = responder_saudacao('olá tudo bem?')
    print(responder)