# PrecedÊncia de Operadores Aritiméticos

# Sempre é executado a ordem de denro para fora:
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta2 = 1+1 **5 + 5 #1024
print(conta2)
conta3 = (1+1) ** (5 + 5) #1024
print(conta3)
conta1 = (1 + 1) ** 5 + 5
print(conta1)

