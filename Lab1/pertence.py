'''
Programa que verifica a pertinencia de um ponto dentro de 
um disco de raio unitário

Exemplo de execução:

Verifica a pertiência de um ponto dentro de um disco unitário
Digite o numero de pontos: 1
Espaco de memoria alocado para variavel n: 28 bytes
Espaco de memoria alocado para variavel i: 24 bytes
Digite a coordenada x do ponto: 0
Digite a coordenada y do ponto: 0.5
Espaco de memoria alocado para variavel x: 24 bytes
Espaco de memoria alocado para variavel y: 24 bytes
O ponto (0,0.5) pertence à região.
'''
print("Verifica a pertiência de um ponto dentro de um disco unitário\n")
# leia a quantidade de pontos
n = int(input('Digite o numero de pontos: '))

print("Espaco de memoria alocado para variavel n: ", n.__sizeof__(), "bytes. \n")

# iterador
i = 0

print("Espaco de memoria alocado para variavel i: ", i.__sizeof__(), "bytes. \n")
while i < n :
    x = float(input('Digite a coordenada x do ponto: '))
    y = float(input('Digite a coordenada y do ponto: '))

    print("Espaco de memoria alocado para variavel x: ", x.__sizeof__(), "bytes. \n")
    print("Espaco de memoria alocado para variavel y: ", y.__sizeof__(), "bytes. \n")
    
    if x >= 0 and y >= 0 and x*x+y*y <= 1:
        print ("O ponto (", x, ",", y, ") pertence à região.\n")
    else:
        print ("O ponto (", x, ",", y, ") não pertence à região.\n")
    i=i+1


