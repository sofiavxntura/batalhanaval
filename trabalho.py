import random

Matriz = [[0 for i in range (0,6)] for j in range(0,6)] #inicializar matriz c/ 0
cont = 0

while cont < 4:
    n1 = random.randint(0,5)
    n2 = random.randint(0,5)
    if Matriz[n1][n2] == 1:
        continue
    else:
        Matriz[n1][n2] = 1
        cont += 1


print(Matriz)

MatrizUser = [['?' for i in range(0,6)] for j in range(0,6)]
linha = int(input("Insira a linha da matriz. (1 a 6) "))
coluna = int(input("Insira a coluna da matriz. (1 a 6) "))
if linha < 1 or linha > 6 or coluna < 1 or coluna > 6:
    print("Insira um número de 1 a 6!")
else:
    

    print(MatrizUser)
