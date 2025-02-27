"""
Listas em Python
Tipo list - Mutável(pode ser mudado o valor no indice que quiser)
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#         01234
#        -54321
string = 'ABCDE' # 5  caracteres
lista = ["jOhn", True, 1992, 1.4]
print(lista)

# aqui mudei o valor no indice [3]
lista[3] = 'aguuu'
print(lista[1], type(lista))
print(lista[-4].upper(), type(lista[-4 ]), lista[-3], lista[3])