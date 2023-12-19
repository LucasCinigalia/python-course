#Generator expression, Iterables e Iterators em Python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(100000)]
generator = (n for n in range (100000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
