"""
Repetições pt1
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> O cod nunca tem fim

"""
cont = 0
while cont <20:
    cont +=1


    if cont == 7:
        print("não vou mostrar 7")
        continue # O continue pula para a proxima repetição e volta para o inicio do while

    print(cont)
    
    if cont == 15:
        break #O break quebra o laço de repetição
print('Contei até ', cont)