nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2)/2
print('A sua média foi {:.2f}'.format(média))
if média >= 6.0:
  print('Parabéns, você foi aprovado!')
else:
  print('Você está de recuperação.')