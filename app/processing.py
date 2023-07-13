import bs4 as bs
import urllib.request
import re
import nltk
import numpy as np
import random
import string
import os
import spacy

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')
dados_html = bs.BeautifulSoup(dados, 'lxml')
paragrafos = dados_html.find_all('p')

conteudo = ''
for p in paragrafos:
    conteudo += p.text

lista_sentencas = nltk.sent_tokenize(conteudo)

pln = spacy.load('pt_core_news_sm')
stop_words = spacy.lang.pt.stop_words.STOP_WORDS

def preprocessamento(texto):
    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)
    texto = re.sub(r" +", ' ', texto)

    documento = pln(texto)
    lista = []
    for token in documento:
       lista.append(token.lemma_)
    
    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista

lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
    lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))
















if __name__ == '__main__':
    os.system('cls')

    # texto_teste = 'https://www.google.com.br/' + lista_sentencas[0]
    # print(texto_teste)

    # resultado = preprocessamento(texto_teste)
    # print(resultado)

    for _ in range(5):
        i = random.randint(0, len(lista_sentencas) - 1)
        print(lista_sentencas[i])
        print()
        print(lista_sentencas_preprocessada[i])
        print('-----' * 5)