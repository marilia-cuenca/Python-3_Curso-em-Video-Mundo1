d = float(input('Qual é a distância da viagem em km? '))
print('Confirmando a sua viagem de {:.0f} km.'.format(d))
if d <= 200:
  print('O preço da sua passagem será de R$ {:.2f}.'.format(d*0.50))
else:
  print('O preço da sua passagem será de R$ {:.2f}.'.format(d*0.45))