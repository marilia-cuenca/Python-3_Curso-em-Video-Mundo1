p = float(input('Qual é o preço do produto? R$ '))
np = p - (p * 5/100)
print('Com 5% de desconto, o preço de R$ {:.2f} passa a ser de R$ {:.2f}.'.format(p, np))