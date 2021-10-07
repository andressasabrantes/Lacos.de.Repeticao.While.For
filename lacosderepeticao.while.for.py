#Exercício de Lógica de Programação - Criar uma tabuada usando os Laços de Repetição FOR e WHILE.

#USANDO O FOR
num = int(input('Digite um número inteiro qualquer: '))
for i in range (1, 11, 1):
    print('{} x {} = {}'.format(num, i, num*i))

#USANDO O WHILE
num = int(input('Digite um número inteiro qualquer: '))
x = 1
while (x <= 10):
    print('{} * {} = {}'.format(num, x, num * x))
    x += 1


