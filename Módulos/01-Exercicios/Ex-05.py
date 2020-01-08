from random import *

lista_alunos = []
for i in range(4):
    aluno = input('Digite o nome de um aluno para o sorteio: ')
    lista_alunos.append(aluno)

shuffle(lista_alunos)
print(f'A ordem de apresentação será: {lista_alunos}')