"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digtar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        - se a letra digitada estiver na palavra secreta, exiba na tela;
        se a letra digitada não estiver na palavra secreta, exiba '*'.
- Faça uma contagem de tentativas do seu usuário
"""
repeticao = 0
palavra_secreta = 'programador'
achou_palavra = ''
# palavra = ''
print('*****Descubra a palavra secreta*****')

while True:
    letra = input(f'Digite uma letra: ({repeticao}x) ')
    repeticao+=1

    if letra.isdigit() == True:
         print('Não é uma letra, digite novamente!')
         continue
    if letra in palavra_secreta:
        print(f'A palavra secreta possui a letra {letra}')
        achou_palavra += letra    
            

    elif letra not in palavra_secreta:
            print(f'A palavra secreta não possui a letra {letra}')

    print(achou_palavra)
    
    elif achou_palavra == palavra_secreta:
        print(f'A palavra secreta é: {palavra_secreta}')
        print(f'Voce tentou {repeticao}x para acertar')




    # if letra in palavra_secreta:
    #     print(f'A Palavra secreta possui a letra  {letra} ')
    #     palavra += letra
    # elif letra not in palavra_secreta;
    #     print(f'A Palavra secreta possui a letra  {letra} ')    
