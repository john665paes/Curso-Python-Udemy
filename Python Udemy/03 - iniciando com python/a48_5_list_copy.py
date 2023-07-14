"""
Cuidados com dados Mutáveis
= - copiado o valor(imutáveis)
= - aponta para o mesmo valor na memória(mutável)
"""
nome= 'john'
outro_nome =  nome
nome = 'zé'
# local salvo na memória
print(id(nome))
print(id(outro_nome))

lista_a = ['john', 'paes', 1992, 14, 'outubro', True]
lista_b =  lista_a.copy() # Copiei o valor da lista A para a lista B

lista_a[0] = 'Eu, eu mesmo'

print(lista_a)
print(lista_b)