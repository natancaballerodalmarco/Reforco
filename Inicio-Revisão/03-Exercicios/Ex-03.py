
notas = int(input('Digite quantas notas houveram no trimestre: '))
lista_notas = []

for i in range(notas):
    n = float(input('Digite a nota: '))
    lista_notas.append(n)

soma = sum(lista_notas)
print(f'A média do trimestre foi {soma/notas}')
