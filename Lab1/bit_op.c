/* Programa de operacoes bit-a-bit
 */

#include <stdio.h>
#include <stdint.h>

void bin(uint8_t value)
  {
    int i;

    printf("0b");
    for (i = 7; i >= 0; i--)
    {
      printf("%d", (value & (1 << i)) >> i );
    }
    return;
}

int main() {
  int valor;
  uint8_t a, b, c;

  // le valores do tipo inteiro
  printf("Digite o valor de a (<= 255): ");
  scanf("%d", &valor);
  // converte para o tipo de 8 bits sem sinal 
  a = (uint8_t) valor; 
  printf ("Digite o valor de b (<= 255): ");
  scanf("%d", &valor);
  b = (uint8_t) valor;

  printf ("a = ");
  bin(a); 
  printf(" e b = ");
  bin(b); 
  printf("\n");

  // faca operacao logica bit-a-bit
  c = a & b;
  printf ("a & b = %d (", c);
  bin(c); 
  printf(")\n");

  c = a | b;
  printf ("a | b = %d (", c);
  bin(c);
  printf(")\n");

  c = a ^ b;
  printf ("a ^ b = %d (", c);
  bin(c);
  printf(")\n");

  c = ~a;
  printf ("~a = %d (", c);
  bin(c);
  printf(")\n");

  printf ("~b = %d (", ~b);
  bin(~b);
  printf(")\n");

  c = a << 2;
  printf ("a << 2 = %d (", c);
  bin(c);
  printf(")\n");

  c = a >> 2;
  printf ("a >> 2 = %d (", c);
  bin(c);
  printf(")\n");

  return 0;
}
