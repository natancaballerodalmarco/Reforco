# -31/12/2019 -Inteiros, Booleanos, String, Float:
# int(4, 8, 580, -4)
# float(4.55, 8.66, -15.678, 7.0)
# bool(True, False)
# str('Olá', '7', '7.0', '')

print('=' *100, '\n')

n1 = input('Digite um número: ')
print(type(n1))
n2 = int(input('Digite um número: '))
print(type(n2))
n3 = float(input('Digite um número com ponto: '))
print(n3)
print(type(n3))

algo = input('Digite algo: ')
print(algo.isalnum())
print(algo.isalpha())
print(algo.isascii())
print(algo.isdecimal())
print(algo.isdigit())
print(algo.isidentifier())
print(algo.istitle())

print('=' *100, '\n')
