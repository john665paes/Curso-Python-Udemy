"""
Tipo Tupla - uma lista imutável

* Sempre que for criar uma lista que não sofra
alteração, posso criar uma tupla
"""
#  posso converter uma lista em uma pupla
nomes_lista = ['arbii','john', 'zé', 'dani']
nomesL = tuple(nomes_lista) #lista

# para criar uma TUPLA é só não adicionar os colchetes
nomesT = 'arbii','john', 'zé', 'dani' #tupla

print(nomesL)
print(nomesT)

