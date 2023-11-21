"""
Enumerate - enumera iteráveis (índices)
"""
lista = ['Lucas', 'Rodrigo', 'Julia']
lista.append('João')

lista_enumerada = enumerate(lista)
for nome in lista_enumerada:
    print(nome)

#-------------------

lista = ['Lucas', 'Rodrigo', 'Julia']

lista_enumerada = list(enumerate(lista, start = 12))

print(lista_enumerada)


#----------------------
lista = ['Lucas', 'Rodrigo', 'Julia']

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}') 


#-------------------------
lista = ['Lucas', 'Rodrigo', 'Julia']

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])