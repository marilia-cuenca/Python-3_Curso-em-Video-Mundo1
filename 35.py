s = float(input('Digite o seu salário atual: R$ '))
if s > 1250:
  print('O seu novo salário será de R$ {:.2f}, pois terá um aumento de 10%.'.format(s + (s*10/100)))
if s <= 1250:
  print('O seu novo salário será de R$ {:.2f}, pois terá um aumento de 15%.'.format(s + (s*15/100)))