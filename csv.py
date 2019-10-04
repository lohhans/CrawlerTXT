# <>================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||
# ||        Armstrong Lohãns        ||
# ||              2019              ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||
# <>================================<>

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def percorrer(texto):
    final = int(texto.find('\n')) + 1
    reverso = texto[::-1]
    inicioPonto = int(reverso.find('.'))
    inicioInterrogacao = int(reverso.find('?'))
    inicioExclamacao = int(reverso.find('!'))
    inicio = 0
    if inicioPonto > 0:
        if inicioInterrogacao > 0:
            if inicioPonto < inicioInterrogacao:
                inicio = inicioPonto
            else:
                inicio = inicioInterrogacao
        else:
            inicio = inicioPonto

    if inicioExclamacao > 0:
        if inicio == 0 or (0 < inicioExclamacao < inicio):
            inicio = inicioExclamacao

    return inicio, final


def csv(site, classificador):
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, "html.parser")

    arquivo = open(classificador + '.csv', 'w')
    arquivo.write('texto' + '\t' + 'classe' + '\n')
    arquivo.close()
    
    for p in soup.find_all('blockquote'):
        texto = p.text.strip('Click to tweet') + '\n'

        inicio, final = percorrer(texto)
        parada = final - inicio
        textoSemAutor = texto[0:parada]

        arquivo = open(classificador + '.csv', 'r')
        conteudo = arquivo.readlines()
        conteudo.append(textoSemAutor + '\t' + classificador + '\n')
        arquivo = open(classificador + '.csv', 'w')
        arquivo.writelines(conteudo)


# MAIN

site = input('Cole o link do "wisdomquotes.com": ')
classificador = input('Nome do classificador: ')

csv(site, classificador)
