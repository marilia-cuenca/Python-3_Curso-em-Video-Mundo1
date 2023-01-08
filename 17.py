from math import hypot, #sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#another possibility: h = sqrt(co*co + ca*ca)
h = hypot(co, ca)
print('A hipotenusa vale {:.2f}.'.format(h))