nome = input('Qual o seu nome: ')
idade = int(input('Qual o sua idade: '))
peso = float(input('Qual o seu peso: '))
print(nome, idade, peso)
print(f'Seu nome é {nome}, sua idade é {idade}, seu peso é {peso}.')

print(f'{nome:<20}')
print(f'{nome:=^20}')
print(f'{nome:>20}')
print(f'{peso:.2f}')

print('Olá', end=' ')
print('Mundo!')
print('Olá\nMundo!')
