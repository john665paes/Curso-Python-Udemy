#  A identidade do valor que está na memória
# o id busca o elemento na memoria do sistema o 
v1 = 'a'
print(id(v1))

v2 = 'ab'
print(id(v2),'espaço na memoria')

""" 
Flag(bandeira - Marca um local)
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_if = None

if condicao:
    passou_if = True
    print('Passou no if')
else:
    print('não passou')

print(passou_if, passou_if is None)
print(passou_if, passou_if is not None)

