num = int(input('Digite um número qualquer de 0 a 9999: '))
if num <= 9999:
  print('Analisando o número {}...'.format(num))
  print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3], num[2], num[1], num[0]))
else:
  print('Valor fora do limite permitido.')