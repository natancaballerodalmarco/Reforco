from math import *

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = hypot(co, ca)
print(f'A hipotenusa é {hip:.3f}')