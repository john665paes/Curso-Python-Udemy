"""
Interpolação básica de strings
s - string
d e i - int
f -float
x e X - hexadecimal ()
% placeholders
""" 
nome = 'John'
preco = 1000.9587874
variavel = '%s, o preço é %.2f' %(nome, preco)
print(variavel)

# HEXADECIMAL

print('O exadecimal de %i é %04X' % (1500,1500))