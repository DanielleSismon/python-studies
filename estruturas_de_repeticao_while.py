# Comando WHILE:
# Um comando de repetição usado para repetir um bloco de código várias vezes. Usa-se o WHILE quando não sabemos o número exato de vezes que o bloco deve ser executado.

# Exemplo - Um loop while onde pede-se para o usuário adivinhar um número entre 1 a 10 até acertar:

import random

numero_secreto = random.randint(1, 10) # Gera um número aleatório entre 1 a 10
tentativas = 0
palpite = None # inicializando a variável palpite com um valor vazio ou "sem valor" antes do loop começar.

while palpite != numero_secreto:
    palpite = int(input('Adivinhe o número entre 1 a 10: '))
    tentativas += 1

    if palpite < numero_secreto:
        print('Muito baixo! Tente novamente: ')
    elif palpite > numero_secreto:
        print('Muito alto! Tente novamente: ')
    else:
        print(f'Parabéns! Você acertou em {tentativas} tentativas!')        
