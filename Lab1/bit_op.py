'''
Programa de demonstracao de operacoes bit-a-bit 
'''
def xor(a, b):
    return (a and not b) or (not a and b)

a = int(input("Digite o valor de a (<= 255): "))
b = int(input("Digite o valor de b (<= 255): "))

print "a = ", bin(a) , "e b = " , bin(b)
 
c = a & b;
print "a & b = " , c , "(",bin(c),")"

c = a | b;
print "a | b = " , c , "(",bin(c) ,")"

c = a ^ b;       
print "a ^ b = " , c , "(",bin(c),")"

c = ~a;       
print "~a = " , c , "(",bin(c),")"
print "~b = " , ~b , "(",bin(~b),")"

c = a << 2;       
print "a << 2 = " , c , "(",bin(c),")"

c = a >> 2;       
print "a >> 2 = " , c , "(",bin(c),")"

