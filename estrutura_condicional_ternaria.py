# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes:
# A primeira parte é o retorno caso a expressão retorne verdadeiro/True, a segunda parte é a expressão lógica
# e a terceira parte é o retorno caso a expressão retorne falso/False.

saldo = 2000
saque = 2500

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')