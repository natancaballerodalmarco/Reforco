frase = 'Saudades da Fernanda'
frase2 = '  Aprendendo Python   '

#Fatiamento:
print(frase[12:20])
print(frase[12::2])
print(frase[::3])

#Análise:
print(len(frase))
print(frase.count('a',12,20))
print(frase.find('Fer',5,20))
print('da' in frase)
print(frase.replace('Fernanda', 'Aragão'))
print(frase.upper())
# captalize != title #title coloca a primeira letra de cada palavra em captalize(de acordo com os espaços)
print(frase2.lstrip())
print(frase2.strip().split())
print('-'.join(frase))
