# Estruturas de Repetição são utilizadas para repetir um trecho de código em um determinado número de vezes.
# Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

# Comando FOR:
# O comando FOR é usado para percorrer um objeto iterável. Faz sentido usar o FOR quando sabemos o número exato de vezes que o bloco de código
# deve ser executado, ou quando queremos percorrer um objeto iterável.

# Exemplo: Um código onde se pede para digitar uma palavra, após a entrada desta palavra o FOR vai percorre-la e imprimir na tela quais vogais possui:

textoDigitado = input('Por favor, digite uma ou mais palavras: ')
VOGAIS = 'AEIOU'

for letra in textoDigitado:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

