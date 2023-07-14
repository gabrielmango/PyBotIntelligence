import os
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from processing import lista_sentencas_preprocessada, lista_sentencas, preprocessamento

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae')
textos_boas_vindas_respostas = ('hey', 'olá', 'opa', 'oi', 'bem-vindo', 'como você está?')

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return random.choice(textos_boas_vindas_respostas) 

def responder(texto_usuario):
  resposta_chatbot = ''
  lista_sentencas_preprocessada.append(texto_usuario)

  tfidf = TfidfVectorizer()
  palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_preprocessada)

  similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)

  indice_sentenca = similaridade.argsort()[0][-2]
  vetor_similar = similaridade.flatten()
  vetor_similar.sort()
  vetor_encontrado = vetor_similar[-2]

  if (vetor_encontrado == 0):
    resposta_chatbot = resposta_chatbot + 'Desculpe, mas não entendi!'
    return resposta_chatbot
  else:
    resposta_chatbot = resposta_chatbot + lista_sentencas[indice_sentenca]
    return resposta_chatbot

def chat_conversa():
  continuar = True
  print('Olá, sou um chatbot e vou responder perguntas sobre inteligência artificial: ')
  while (continuar == True):
    texto_usuario = input()
    texto_usuario = texto_usuario.lower()
    if (texto_usuario != 'sair'):
      if (responder_saudacao(texto_usuario) != None):
        print('Chatbot: ' + responder_saudacao(texto_usuario))
      else:
        print('Chatbot: ')
        print(responder(preprocessamento(texto_usuario)))
        lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
    else:
      continuar = False
      print('Chatbot: Até breve!')

def conversa(mensagem):
  mensagem = mensagem.lower()
  if mensagem != 'sair':
    if responder_saudacao(mensagem) != None:
      return 'Chatbot: ' + responder_saudacao(mensagem)
    else:
      reposta = 'Chatbot: ' + responder(preprocessamento(mensagem))
      lista_sentencas_preprocessada.remove(preprocessamento(mensagem))
      return reposta
  else:
    return 'Chatbot: Até breve!'


if __name__ == '__main__':
  os.system('cls')

  print(responder('Alan Turing'))