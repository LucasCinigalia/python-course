"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Hello world.'
print(variavel[5:9])
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[-1:-13:-1])
print(variavel[::-1])
