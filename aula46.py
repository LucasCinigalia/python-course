# Manipulando chaves e valores em dicionarios
pessoa = {

}


chave = 'nome'

pessoa[chave] = 'Lucas'
pessoa['sobrenome'] = 'Cinigalia'


print(pessoa[chave])

pessoa[chave] = 'João'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')