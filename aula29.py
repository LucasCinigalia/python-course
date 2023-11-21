"""
for in com listas
"""

lista = ['Lucas', 'Rodrigo', 'Julia']
lista.append('Mauricio')
lista.append('Thais')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])