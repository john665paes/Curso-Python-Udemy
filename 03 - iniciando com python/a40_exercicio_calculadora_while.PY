"""
Calculadora com While
"""
print("*****Calculadora*****\n" )

while True:
    num1 = input("Informe um numero para caucular: ")
    num2 = input("Informe outro numero para caucular: ")
    print("\nOperdores: + - * / ")
    op = input("Informe um operador: ")
#   Esse é o cod do professor:
    numValidos = None
    n1 = 0
    n2 = 0
    # AGORA TEM TODA UMA VALIDAÇÃO DOS DADOS SOLICITADOS
    # SO APÓS VALIDAR O CAUCULO SERÁ FEITO
    try:
        # informei dentro do TRY o tipo de conversão para a verificação poder ser validada
        n1 =  float(num1)
        n2 =  float(num2)
        numValidos = True
    except:
        numValidos = None

    if numValidos == None:
        print('Um ou ambos os numeros digitados não são validos')
        continue

    op_permitido = '+-*/'

    if op not in op_permitido:
        print('o operador não é válido')
        continue
    if len(op) > 1:
        print('Digite apenas um operador')
        continue
    
    # AQUI COMEÇA O CAULCULO
    print('Cauculando...')
    if op == '+':
        print(f'{n1} + {n2} = ', n1+n2)
    elif op == '-':
        print(f'{n1} - {n2} = ', n1-n2)
    elif op == '*':
        print(f'{n1} * {n2} = ', n1*n2)
    elif op == '/':
        print(f'{n1} / {n2} = ', n1/n2)

#   Tambem fiz essa parte
    condParar = input('Deseja calcular outro valor? [S/N]: ').lower().startswith('n')
    # a função lower() converte qualquer string para minuscula
    # a função startswith() verifica a primeira letra da str e retorna um bool

    #Nesse caso ele confimou a condição para parar o while
    if condParar:
        break

print(' \nCalculadora encerrada')


