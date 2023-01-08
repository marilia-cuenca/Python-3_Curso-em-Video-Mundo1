l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
área = l * a
tinta = área / 2
print('Para a área de {} m², serão necessários {:.1f} litros de tinta.'.format(área, tinta))