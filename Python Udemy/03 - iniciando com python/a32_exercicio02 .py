 
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Que horas são? '))

dia = hora>=0 and hora<=11
tarde = hora>=12 and hora<=17
noite = hora>=18 and hora <=23

print(f'São {hora}hs')
if dia:
    print(f'Bom dia!')
elif tarde:
    print(f'Boa tarde!')
elif noite:
    print(f'Boa Noite!')

