# Interpolação na área de computação significa inserir ou ajustar elementos dentro de um conjunto de outros elementos.
# Interpolação de Variáveis em programação refere-se à inserção de valores de variáveis dentro de uma string de maneira dinâmica. 
# Em vez de concatenar manualmente valores e strings, você pode usar um método de interpolação para tornar isso mais simples e legível.
# Em Python as duas formas mais utilizadas para tal são:

# método format
nome = 'Danielle'
idade = 38
profissao = 'programadora'
linguagem = 'Python e Java'

print('Olá! Me chamo {}. Eu tenho {} anos de idade, trabalho como {} utilizando a(s) linguagen(s) {}.'.format(nome, idade, profissao, linguagem))
print('=====================================')

print('Olá! Me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada(o) no curso de {0}'.format(linguagem, profissao, 
idade, linguagem))

# utilizando "f strings"
