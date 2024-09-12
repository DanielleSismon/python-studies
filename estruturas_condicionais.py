# Uma estrutura condicional permite o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas.
# Temos em Python as seguintes estruturas condicionais:

# if:
# Para criar uma estrutura condicional simples, composta por um único desvio de fluxo, podemos utilizar a palavra reservada if.
# O comando irá testar a expressão lógica e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

# Como exemplo, abaixo está um trecho de código para verificar se o número é positivo:

numero = 5

if numero > 0:
    print("O número é positivo.")

 if / else:
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if else.
# Caso a expressão lógica testada no if for verdadeira, então o bloco if será executado e o else não. Caso contrário, será executado o bloco else:

# Como exemplo, segue um código:

saldo = 2000.00
saque = float(input("Ola! Informe o valor do saque por favor: "))

if saldo >= saque:
    print("Um momento por gentileza, estamos realizando o saque!")

else:
    print("Saldo insuficiente.")


# if / elif / else:
# Esta estrutura é usada quando se quer mais de dois desvios. Sendo o elif aglutinação das palavras else + if.

# Exemplo: 

idade = int(input("Digite sua idade por favor. "))

if idade < 12:
    print("Você é uma criança.")

elif idade >= 12 and idade < 18:
    print("Você é um adolescente.")

else:
    print("Você é um adulto.")

# ANINHAMENTO DE ESTRUTURAS CONDICIONAIS:
# Ilustra o controle de fluxo em diferentes níveis. Criando-se dentro do bloco de condição, outro bloco de condição:
# No exemplo abaixo, há um código para além de identificar a idade, identifica o gênero:

idade = int(input("Por favor digite sua idade: "))
genero = input("Por favor digite seu gênero F para feminino e M para masculino: ")

if idade < 12:
    if genero == "f" or genero == "F":
        print("Você é uma menina.")
    elif genero == "m" or genero == "M": 
        print("Você é um menino.")

elif idade >= 12 and idade < 18:
    if genero == "f" or genero == "F":
        print("Você é uma adolescente.")
    elif genero == "m" or genero == "M":
        print("Você é um adolescente.")

elif idade >= 18:
    if genero == "f" or genero == "F":
        print("Você é uma mulher.")
    elif genero == "m" or genero == "M":
        print("Você é um homem.")

else:
    print("Valor inválido.")                   