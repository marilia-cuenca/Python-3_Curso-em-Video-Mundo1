from random import choice
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
lista = [a, b, c, d]
sorteio = choice(lista)
print('O aluno escolhido para apagar o quadro é {}.'.format(sorteio))