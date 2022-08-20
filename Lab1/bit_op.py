'''
Programa de demonstracao de operacoes bit-a-bit 
'''
def xor(a, b):
    return (a and not b) or (not a and b)

a = int(input("Digite o valor de a (<= 255): "))
b = int(input("Digite o valor de b (<= 255): "))

print(f"a = {a:08b} e b = {b:08b}")
 
c = a & b;
print(f"a & b = {c} ({c:08b})")

c = a | b;
print(f"a | b = {c} ({c:08b})")

c = a ^ b;       #XOR
print(f"a ^ b = {c} ({c:08b})")

c = ~a;         #NOT
print(f"~a = {c}, ({c:08b})")
print(f"~b = {~b}, ({~b:08b})")

c = a << 2;     #Deslocamento de dois bits  
print(f"a << 2 = {c}, ({c:08b})")

c = a >> 2;      #Deslocamento de dois bits
print(f"a >> 2 = {c}, ({c:08b})")
