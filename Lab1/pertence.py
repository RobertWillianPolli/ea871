'''
Programa que verifica a pertinencia de um ponto dentro de 
um disco de raio unitário

Exemplo de execução:

Verifica a pertiência de um ponto dentro de um disco unitário
Digite o numero de pontos: 1
Digite a coordenada x do ponto: 0
Digite a coordenada y do ponto: 0.5
O ponto (0,0.5) pertence à região.
'''

print("Verifica a pertiência de um ponto dentro de um disco unitário\n")
# leia a quantidade de pontos
n = int(input('Digite o numero de pontos: '))

# iterador
i = 0

while i < n :
    x = float(input('Digite a coordenada x do ponto: '))
    y = float(input('Digite a coordenada y do ponto: '))
    
    if x >= 0 and y >= 0 and x*x+y*y <= 1:
        print ("O ponto (", x, ",", y, ") pertence à região.\n")
    else:
        print ("O ponto (", x, ",", y, ") não pertence à região.\n")
    i=i+1

