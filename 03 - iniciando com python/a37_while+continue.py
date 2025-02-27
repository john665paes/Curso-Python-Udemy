"""
Repetições pt1
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> O cod nunca tem fim

"""
cont = 0
while cont <=100:
    cont +=1


    if cont == 7:
        print("não vou mostrar, usei um 'CONTINUE' 7")
        continue # O continue pula para a proxima repetição e volta para o inicio do while
    
    if cont >=27 and cont <=47:
        # print('pulei do 27 até o 47 no contador')
        continue
    # Tanto o break quanto o continue são usados para o while mais proximo dela
    print(cont)
    
    if cont == 50:
        break #O break quebra o laço de repetição
print('Contei até ', cont)