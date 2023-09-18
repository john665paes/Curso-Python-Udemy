"""
enumerate - enumera iteráveis (índices)
"""
lista = ['john', 'zé', 'dani']
lista.append('Rasgaaa')

lista_enumerada1 = enumerate(lista, start=2)
# Aqui ele exibe o proximo valor da lista, no caso o primeiro
print(next(lista_enumerada1))
print(lista)

# para acessar o item da minha lista inumerada usando for
for item in lista_enumerada1:
    # a exibição de cada item na lista, no espaço e o valo alocado no espaço
    print(item) # esse caso é a mesma coisa do next

# OBS: quando se usa o inumerate, não se usa direto na váriavel pois ela é esgotável.
# o exemplo acima é descartavel, abaixo é o correto.

for item in enumerate(lista):
    print(item)