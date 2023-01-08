nome = input('Digite o nome do aluno: ')
n1 = float(input('Qual é a primeira nota? '))
n2 = float(input('Qual é a segunda nota? '))
média = (n1 + n2)/2
print('A média do aluno {} é {:.1f}.'.format(nome, média))