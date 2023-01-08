km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro ficou alugado? '))
preço = (km * 0.15) + (dias * 60)
print('O preço total é R$ {:.2f}.'.format(preço))
