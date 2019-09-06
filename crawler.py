# <>================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||
# ||        Armstrong Lohãns        ||
# ||              2019              ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||
# <>================================<>

# LOVE: http://wisdomquotes.com/love-quotes/
# FUNNY: http://wisdomquotes.com/funny-quotes/
# PEACE: http://wisdomquotes.com/peace-quotes/

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def percorrer(texto):
    final = int(texto.find('\n'))+1
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
        if inicio == 0 or (inicioExclamacao > 0 and inicio > inicioExclamacao):
            inicio = inicioExclamacao

    return(inicio, final)

def crawler(site, nome):
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, "html.parser")

    arquivo = open(nome + '.txt', 'w')
    arquivo.close()

    for p in soup.find_all('blockquote'):
        texto = p.text.strip('Click to tweet') + '\n'

        inicio, final = percorrer(texto)
        parada = final-inicio
        textoSemAutor = texto[0:parada]

        arquivo = open(nome + '.txt', 'r')
        conteudo = arquivo.readlines()
        conteudo.append(textoSemAutor + '\n')
        arquivo = open(nome + '.txt', 'w')
        arquivo.writelines(conteudo)


site = input('Cole o link do "wisdomquotes.com": ')
nome = input('Nome do .txt de saída (só o nome): ')

crawler(site, nome)
