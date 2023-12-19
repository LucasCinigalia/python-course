# Dictionary com prehension e Set comprehension
produto = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "Categoria": 'Escritório',
}


dictionary = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != "C ategoria"
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dictionary = {
    chave: valor
    for chave, valor in lista
}
print(dictionary)

set_1 = {2 ** i for i in range(10)}
print(set_1)
# print(set(range(10)))
