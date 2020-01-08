dias = int(input('Digite quantos por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos KM o carro percorreu durante o período: '))

print(f'O total a pagar é R${dias*60 + km*0.15:.2f}')