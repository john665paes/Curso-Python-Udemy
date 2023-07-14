"""
Listas em Python
Tipo list - Mutável(pode ser mudado o valor no indice que quiser)
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:
    append, insert, pop, del, clear, extend, +
Creat - Read - Update - Delete
criar - ler  - Alterar - apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
print(lista)
lista[2] = "Ai dento"
print(lista)
del lista[3]
print(lista)
print(lista[2])
lista.append("Rasgaaa!")
lista.append("Gzuzz")
valor_removido = lista.pop() # O método pop() remove o ultimo item adicionado a lista
lista.append("pisaaa porra")
print(lista, 'Removi o valor = ', valor_removido)
    