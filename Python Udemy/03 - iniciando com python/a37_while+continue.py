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
        continue
    
    print(cont)
    
    if cont == 15:
        break
print('Já contei desgraça!')