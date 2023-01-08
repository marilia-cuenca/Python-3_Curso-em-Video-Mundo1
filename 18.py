from math import sin, cos, tan, radians
a = float(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Em relação ao ângulo {},\no valor do seno é {:.2f},\ndo cosseno é {:.2f}\ne da tangente é {:.2f}.'.format(a, s, c, t))