from random import randint
from time import sleep
computador = randint(0, 5)
print('Estou pensando em um número entre 0 e 5... Tente adivinhar qual é!')
usuário = int(input('Escolha um número: '))
print('*** PROCESSANDO ***')
sleep(2)
if computador == usuário:
  print('Parabéns, você acertou!')
else:
  print('Tente de novo.')