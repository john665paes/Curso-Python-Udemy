"""
Introdução ao desempacotamento"""

nome1, nome2, nome3 = ['john', 'zé', 'dani']

print(nome2)

# empacotando e desempacotando a lista
_, nome, *resto = ['arbii','john', 'zé', 'dani']
print(nome, resto)