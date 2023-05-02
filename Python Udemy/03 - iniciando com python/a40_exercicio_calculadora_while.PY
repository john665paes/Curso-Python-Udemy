"""
Calculadora com While
"""
print("*****Calculadora*****\n" )

while True:
    n1 = int(input("Informe um numero para caucular: "))
    n2 = int(input("Informe outro numero para caucular: "))
    print("\nOperdores: + - * / ")
    op = input("Informe informe um operador: ")
#   Esse é o cod do professor:
    numValidos = None

    try:
        n1Float = float(n1)
        n2Float = float(n2)
        numValidos = True
        if op == '+':
            print(f'{n1} + {n2} = ', n1+n2)
        elif op == '-':
            print(f'{n1} - {n2} = ', n1-n2)
        elif op == '*':
            print(f'{n1} * {n2} = ', n1*n2)
        elif op == '/':
            print(f'{n1} / {n2} = ', n1/n2)

    except:
        numValidos = None

    if numValidos == None:
        print('Um ou ambos os numeros digitados não são validos')
        continue
    
    
#   esse foi o meu cód
""" if op == '+':
print(f'{n1} + {n2} = ', n1+n2)
elif op == '-':
print(f'{n1} - {n2} = ', n1-n2)
elif op == '*':
print(f'{n1} * {n2} = ', n1*n2)
elif op == '/':
print(f'{n1} / {n2} = ', n1/n2)"""

    cond = input('Deseja calcular outro valor? [S/N]: ').lower().startswith('n')
    # a função lower() converte qualquer string para minuscula
    # a função startswith() verifica a primeira letra da str e retorna um bool
    if cond:
        break

print(' \nCalculadora encerrada')