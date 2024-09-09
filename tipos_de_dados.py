print('hello world!')

# Note que não é necessário terminar cada sentença com ponto e vírgula, como por exemplo em Java é obrigatório, em JavaScript é opcional.

# TIPOS DE DADOS:

# Os tipos mais usados são:

# Tipo Texto (sempre entre aspas podendo ser duplas " ou simples '): str
# Tipo Numérico: int (nºs inteiros), float (nºs com ponto flutuante), complex
# Tipo Sequência (numérica, de texto, pode ser em ordem ou fora de ordem): lis, tuple, range
# Tipo Mapa (chave, valor): dict
# Tipo Coleção (parecido com a lista porém, não permite itens repetidos): set, fronzenset
# Tipo Booleano (usado para representar verdadeiro ou falso): bool
# Tipo Binário: bytes, bytearray, memoryview 

# VARIÁVEIS e CONSTANTES:
# sintaxe de uma Variável:

nome = 'Danielle'
idade = 38

nome = 'Zeca'

# é possível definir as variáveis em uma mesma linha:
nome, idade = 'Mariana', 24

print(nome, idade)

# sintaxe de uma Constante (obs: constante não existe em Python, acontece uma convenção entre os programadores de se digitar a constante com 
# todas as letras em MAIÚSCULO / UPPER CASE):

PI = 3.14159265359

PI = 9

print(PI)

# Outro exemplo de "constate":

ESTADOS_BRASILEIROS = ["AM", "AC", "SP", "RJ", "MS", "MT"]

ESTADOS_BRASILEIROS = ["California"]

print(ESTADOS_BRASILEIROS)

# CONVERTENDO TIPOS:

# Tipo Inteiro para o tipo Float:

preco = 10
print(preco)

# usamos o construtor float()
preco = float(preco)
print(preco)

# acontece também ao dividirmos dois inteiros com resultado decimal, ou seja, com ponto flutuante:
preco = 5 / 2
print(preco)


# Tipo Float para tipo Inteiro:
# usamos o construtor int()

valor = 25.35
print("valor antes da conversao: ")
print(valor)

valor = int(valor)
print("valor apos o construtor int(): ")
print(valor)

print("===========================================")
# Conversão por divisão:

numero = 10
print(numero)

print(numero / 2)

# ao se dividir digitando duas barras o número impresso será do tipo Inteiro:
print(numero // 2)

print("==========================================================")

# CONVERSÃO DE NÚMERO PARA STRING:
preco = 10.50
idade = 38
print(type(preco))
print(type(idade))
# usamos o construtor str():
preco = str(preco)
idade = str(idade)

# para verificar se é do tipo string:
print(type(preco))
print(type(idade))

# caso prefira, é possível concatenar os construtores str() e type() no print():
valor = 25.75
idade = 19

print(valor)
print(type(valor))
print(type(str(valor)))

print("========================================")

# CONVERSÃO DE STRING PARA NÚMERO:
# segue-se a mesma lógica, porém, usando os construtores float() ou int():

numero = '10.25'
idade = '45'

print(numero)
print(type(numero))

numero = float(numero)
print(type(numero))


print('===============================================')
# observe que ao usar a função input(), o que digitamos no prompt retorna como string, meso sendo números:

numero = input('Por favor, digite um numero: ')

print(numero)
print(type(numero))

numero = int(numero)
print(type(numero))

print('====================================================')

# pode-se unir as funções para já poder receber o valor no input e converter para inteiro, por exemplo:
numero = int(input('Digite outro número por favor: '))

print(numero)
print(type(numero))
