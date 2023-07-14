"""
for in com listas
"""
# Como a lista também é um iterável é possível usar o for

lista = ['john', 'zé', 'dani']
indices = range(len(lista))

# cont = 0
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    # cont+= 1