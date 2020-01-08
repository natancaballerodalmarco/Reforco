with open('cadastro.txt', 'r') as arquivo:

    tipo_dados = ['Codigo', 'Nome', 'Idade', 'Sexo', 'Email', 'Telefone']
    lista_cadastros = []

    for pessoa in arquivo:
        dic = {}
        pessoa = pessoa.strip()
        pessoa = pessoa.split(';')
        for i in range(6):
            dic[tipo_dados[i]] = pessoa[i]
        
        lista_cadastros.append(dic)

    print(lista_cadastros)
