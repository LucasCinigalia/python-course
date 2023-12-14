# dir, hasattr e getattr em Python
string = 'Lucas'
metodo = 'upper'

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metoddo', metodo)
