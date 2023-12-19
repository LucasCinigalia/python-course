# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Cinigalia',
    'idade': 90,
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])

import copy

dicionaio1 = {
    'chave1': 1,
    'chave2': 2,
    'lista1': [0, 1, 2],
}
dicionario2 = dicionaio1.copy()

dicionario2['chave1'] = 1000
dicionario2['lista1'][1] = 999999

print(dicionaio1)
print(dicionario2)



pessoa1 = {
    'nome': 'Lucas',
    'sobrenome': 'Cinigalia',
}

# print(pessoa1.get['nome'])
# print(pessoa1.get('nome', 'Não existe'))


# nome = pessoa1.pop('nome')
# print(nome)
# print(pessoa1)


# ultima_chave = pessoa1.popitem()
# print(ultima_chave)
# print(pessoa1)



# pessoa1.update({
#     'nome': 'novo valor',
#     'idade': 18,
# })

# pessoa1.update(nome='novo valor', idade=18)

# tupla = (('nome', 'novo valor'), ('idade', 18))
lista = [['nome', 'novo valor'],['idade', 18]]
pessoa1.update(lista)
print(pessoa1)