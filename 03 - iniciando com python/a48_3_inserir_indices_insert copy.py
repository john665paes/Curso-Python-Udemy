"""
Listas em Python
Tipo list - Mutável(pode ser mudado o valor no indice que quiser)
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - Concatena listas
Creat - Read - Update - Delete
criar - ler  - Alterar - apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('john')
print(lista)
nome=lista.pop()
print(lista, nome)
print(nome)
del lista[-1]# Deletei o último indice da lista
print(lista)
#            o primeiro argumento é o index, o segundo é o valor
lista.insert(0,'johnjohn')# O insert é o método que recebe dois argumentos
print(lista)

