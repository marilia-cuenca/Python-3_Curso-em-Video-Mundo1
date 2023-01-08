n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
di = n1 // n2
exp = n1 ** n2
print('A soma entre {} e {} é {} e a divisão é {:.2f}.'. format(n1, n2, soma, div))
print('A divisão inteira entre {} e {} é {} e a potência é {}.'.format(n1, n2, di, exp))