cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('A sua cidade começa com a palavra "Santo"?')
print(cidade[:5].upper() == 'SANTO')
