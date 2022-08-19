'''
Programa que verifica a quantidade de ocorrências de uma palavra dentro 
de uma frase

Exemplo de execução:

Verifica a quantidade de ocorrências de uma substring dentro de uma string
Digite a frase: ANATOMISTA ANA MARIANA GOSTA DE BANANA
Digite a palavra buscada: ANA
A quantidade de ocorrências é 4
'''

print("Verifica a quantidade de palavras\n")
# leia a palavra
frase = input('Digite a frase: ')

# leia a palavra buscada
palavra = input('Digite a palavra buscada: ')

# quantidade de letras em cada string
m = len(frase)
n = len(palavra)

# conte a quantidade de ocorrências
numOcor = frase.count (palavra)

print (frase, " e ", palavra, " tem, respectivamente ", m, " e ", n, "letras\n" )
print ("A quantidade de ocorrências de ", palavra, " em ", frase, " é ", numOcor, "\n")

