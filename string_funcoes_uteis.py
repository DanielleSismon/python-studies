palavra = '    pYtHon     '

print(palavra.upper()) # Tranforma todas as letras em maiúsculas

print(palavra.lower()) # Transforma todas as letras em minúsculas

print(palavra.title()) # Apenas a primeira letra da palavra em maiúsculo

# Eliminando espaços em branco:
print(palavra.strip()) # elimina espaços em branco de ambos os lados

print(palavra.lstrip()) # elimina espaços em branco à esquerda

print(palavra.rstrip()) # eimina espaçoos em branco à direita

# Centralização e Junções:
word = 'banana'

print(word.center(10, '#')) # .center(1º_Argumento , "2º_Argumento") centraliza a palavra dentro do elemento digitado no caso #. 
# O 1º argumento é a quantidade total de caracteres que vai ocupar ao todo, 
# o 2º argumento entre aspas é o caracter que se deseja colocar à esquerda e à direita. É opcional, caso esteja sem este argumento, 
# é centralizado com espaços em branco.

print(".".join(word)) # função/método .join() junta




