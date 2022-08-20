/* Programa para mascaramento
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
  int type;


