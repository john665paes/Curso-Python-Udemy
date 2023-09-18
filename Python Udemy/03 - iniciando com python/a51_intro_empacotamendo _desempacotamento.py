"""
Introdução ao desempacotamento"""

nome1, nome2, nome3 = ['john', 'zé', 'dani']
print(nome2)

# Usando uma variável para empacotar o resto dos valores
nome1, *resto = ['john', 'zé', 'dani']
print(nome1, resto)

# empacotando e desempacotando a lista
# O undeline ignora o expaço ocupado na posição informada na variável(recurso não utilizado)
_, nome, *resto = ['arbii','john', 'zé', 'dani']
print(nome, resto)