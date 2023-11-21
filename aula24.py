"""
Iterável -> str, range, etc (_iter_)
Iterador -> quem sabe entregar um valor por vez
Next -> me entregue o proximo valor
Iter -> me entregue seu iterador

For + Range
range -> range(start, stop, step)
"""

# numeros = range(0, 105, 15)

# for numero in numeros:
#     print(numero)



# texto = iter('Lucas')

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))



texto = 'Lucas'  # iterável
iterador = iter(texto)  # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break


for letra in texto:
    print(letra)