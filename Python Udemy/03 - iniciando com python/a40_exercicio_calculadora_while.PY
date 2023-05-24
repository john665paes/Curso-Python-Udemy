"""
Calculadora com While
"""
print("*****Calculadora*****\n" )

while True:
    n1 = float(input("Informe um numero para caucular: "))
    n2 = float(input("Informe outro numero para caucular: "))
    print("\nOperdores: + - * / ")
    op = input("Informe informe um operador: ")
#   Esse é o cod do professor:
    numValidos = None

    try:
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

    condParar = input('Deseja calcular outro valor? [S/N]: ').lower().startswith('n')
    # a função lower() converte qualquer string para minuscula
    # a função startswith() verifica a primeira letra da str e retorna um bool

    #Nesse caso ele confimou a condição para parar o while
    if condParar:
        break

print(' \nCalculadora encerrada')


#   esse foi o meu cód
""" if op == '+':
print(f'{n1} + {n2} = ', n1+n2)
elif op == '-':
print(f'{n1} - {n2} = ', n1-n2)
elif op == '*':
print(f'{n1} * {n2} = ', n1*n2)
elif op == '/':
print(f'{n1} / {n2} = ', n1/n2)"""

