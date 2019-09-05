# Exemplo a ser buscado:
#
# <blockquote><p>Every next level of your life will demand a different you. <a
# class="clicktotweet" title="Click to tweet!" href="https://twitter.com/intent/tweet?text=Every next level of your
# life will demand a different you.+http://bit.ly/mostinspirationalquotes" target="_blank" rel="nofollow noopener
# noreferrer">Click to tweet</a></p></blockquote>

# TODO: Retirar o nome do autor
# TODO: Salvar cada frase em um txt
# Obs: Para retirar o nome do autor, a ideia eh dar um split no primeiro ".", porem algumas frases tem mais de um "."!

import urllib.request
# import urllib.parse

content = urllib.request.urlopen("http://wisdomquotes.com/inspirational-quotes/").read()
content = str(content)
find = '<blockquote><p>'
posicao = int(content.index(find) + len(find))
findPoint = '<a class="clicktotweet"'
parada = int(content.index(findPoint) + len(findPoint))
texto = content[posicao:parada-23]

print(texto)
