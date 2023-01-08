velocidade = float(input('Qual é a velocidade atingida (em km/h)? '))
multa = (velocidade - 80)*7
if velocidade > 80:
  print('Você foi multado. O preço da multa é de R$ {:.2f}.'.format(multa))
else:
  print('A sua velocidade está dentro do limite. Dirija com cuidado!')