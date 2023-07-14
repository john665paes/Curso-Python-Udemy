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

#         0   1   2   3
listaA = [10, 20, 30, 40]
listaB = [50, 60, 70, 80]
# com a concatenação
listaC = listaA + listaB
print(listaC)

# Nesse Caso, o extend() não retorna valor, executa uma ação sem valor 
# ele mexe no valor do objeto em si, nesse caso a variável listaA
listaA.extend(listaB)
print(listaA)