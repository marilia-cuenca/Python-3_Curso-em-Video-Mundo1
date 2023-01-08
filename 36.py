número = int(input('Me diga um número qualquer: '))
resultado = número % 2
#print('O resultado foi {}.'.format(resultado))
if resultado == 1:
  print('O número {} é ímpar.'.format(número))
else:
  print('O número {} é par.'.format(número))