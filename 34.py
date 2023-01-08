n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 < n2 < n3:
  print('O número {} é o menor e o {} é o maior'.format(n1, n3))
if n3 < n2 < n1:
  print('O número {} é o menor e o {} é o maior'.format(n3, n1))
if n3 < n1 < n2:
  print('O número {} é o menor e o {} é o maior'.format(n3, n2))
if n2 < n1 < n3:
  print('O número {} é o menor e o {} é o maior'.format(n2, n3))
if n2 < n3 < n1:
  print('O número {} é o menor e o {} é o maior'.format(n2, n1))
if n1 < n3 < n2:
  print('O número {} é o menor e o {} é o maior'.format(n1, n2))