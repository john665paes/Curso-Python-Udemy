"""
for in com listas
"""
# Como a lista também é um iterável é possível usar o for

lista = ['john', 'zé', 'dani']

cont = 0
for indice in lista:
    print(cont, indice)
    cont+= 1