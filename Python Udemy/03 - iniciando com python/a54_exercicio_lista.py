lista = ['arroz', 'feijão', 'açucar']
comprar = True
while comprar:
    print(" O que você quer fazer com a lista?")
    print("(1) Adicionar item ? ")
    print("(2) Apagar item? ")
    print("(3) Listar Itens?")
    acao = int(input("digite opção: "))
    
    for item in enumerate (lista):

        print(item)
