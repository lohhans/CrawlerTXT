# Exemplo a ser buscado:
#
# <blockquote><p>Every next level of your life will demand a different you. <a
# class="clicktotweet" title="Click to tweet!" href="https://twitter.com/intent/tweet?text=Every next level of your
# life will demand a different you.+http://bit.ly/mostinspirationalquotes" target="_blank" rel="nofollow noopener
# noreferrer">Click to tweet</a></p></blockquote>

# TODO: Retirar o nome do autor
# TODO: Salvar cada frase em um txt
# TODO: Receber site do teclado

# Obs: Para retirar o nome do autor, a ideia eh dar um split no primeiro ".", porem algumas frases tem mais de um "."!

import urllib.request
from bs4 import BeautifulSoup


site = urllib.request.urlopen('http://wisdomquotes.com/inspirational-quotes/').read()
soup = BeautifulSoup(site, "html.parser")

texto = soup.find_all('blockquote')
for p in soup.find_all('blockquote'):
   print(p.text+'\n')