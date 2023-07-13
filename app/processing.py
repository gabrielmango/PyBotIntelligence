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

if __name__ == '__main__':
    os.system('cls')

    # print(dados)
    # print(dados_html)

    # print(paragrafos)
    # print(len(paragrafos))

    # print(conteudo)
    # print(len(conteudo))

    # print(lista_sentencas)
    # print(len(lista_sentencas))

    # print(pln)
    # print(stop_words)
    # print(len(stop_words))
