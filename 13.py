nome = input('Digite o nome do funcionário: ')
salário = float(input('Digite o salário do funcionário: R$ '))
aumento = salário + (salário * 15/100)
print('O novo salário de {} é R$ {:.2f}.'.format(nome, aumento))