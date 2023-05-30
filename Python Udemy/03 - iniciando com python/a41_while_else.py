"""While/else"""

string = 'chama trouxa'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i +=1
# Se houver um  break o "else" não será executado

# se o while for executado por completo, o "else" será executado
else: #posso usar o else caso queria informar se achei alguma informação
    print("Que viagem esse else")

print("O if encontrou o espaço na verificação e não executou o else")
