 
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')

# Esse é meu cod
if hora.isdigit():
    hora = int(hora)
    print(f'São {hora}hs')
    if hora>=0 and hora<=11:
        print(f'Bom dia!')
    elif hora>=12 and hora<=17:
        print(f'Boa tarde!')
    elif hora>=18 and hora <=23:
        print(f'Boa Noite!')
    elif hora>23:
        print("O formato de hora digitado é inválido")
else:
    print("O formato de hora digitado é inválido")

# Esse cod é do professor
try:
    hora = int(hora)
    print(f'São {hora}hs')
    if hora>=0 and hora<=11:
        print(f'Bom dia!')
    elif hora>=12 and hora<=17:
        print(f'Boa tarde!')
    elif hora>=18 and hora <=23:
        print(f'Boa Noite!')
    elif hora>23:
        print("O formato de hora digitado é inválido")
except:
    print("O formato de hora digitado é inválido")


