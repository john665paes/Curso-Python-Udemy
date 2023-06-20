"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digtar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        - se a letra digitada estiver na palavra secreta, exiba na tela;
        se a letra digitada não estiver na palavra secreta, exiba '*'.
- Faça uma contagem de tentativas do seu usuário

"""
import os

repeticao = 0
palavra_secreta = 'programador'
letras_acertadas = ''

# palavra = ''
print('*****Descubra a palavra secreta*****')

while True:
    letra = input(f'Digite uma letra: ')
    repeticao+=1

    if letra.isdigit():         
        print('Não é uma letra, digite novamente!')
        continue
    
    if len(letra)>1:
         print('Digite apenas uma letra!')
         continue
     
    if letra in palavra_secreta:
        letras_acertadas +=letra

# fiz um for na palavra secreta
# se a letra estiver na palavra secreta sera exibida
# senão, exibira um '*'
    palavra_formada= ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("Parabens você acertou a Palavra: ", palavra_secreta)
        print(f'Usando {repeticao} tentativas')
        break





    #     print(palavra_secreta[i])    

    #     print(f'Palavra secreta possui a letra {letra}')
            

    # elif letra not in palavra_secreta:
    #         print(f'A palavra secreta não possui a letra {letra}')

    # print(achou_palavra)
    
    # elif achou_palavra == palavra_secreta:
    #     print(f'A palavra secreta é: {palavra_secreta}')
    #     print(f'Voce tentou {repeticao}x para acertar')




    # if letra in palavra_secreta:
    #     print(f'A Palavra secreta possui a letra  {letra} ')
    #     palavra += letra
    # elif letra not in palavra_secreta;
    #     print(f'A Palavra secreta possui a letra  {letra} ')    
