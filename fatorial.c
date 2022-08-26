/*
 * fatorial.c 
 */
 
/* Bloco de diretivas de pre-processamento */
#include <stdio.h>

/* Bloco de prototipos das funcoes */
int fatorial(int n, int *fatorial);

/* Definicao da funcao main */
int main (){
  int n,        /* guarda o numero dado */
      res; 
  
  printf("\n\tCalculo do fatorial de um numero\n");
  printf("\nDigite um inteiro nao-negativo: ");

  scanf("%d", &n);

  fatorial(n, &res);

  printf("O valor de %d!: %d\n", n, res);

  return 0;
}

/* Definicao da funcao fatorial */
int fatorial(int n, int *fatorial) {
  int contador; 
    
  /* inicializacoes */
  *fatorial = 1;
  contador = 2;
  
  while (contador <= n) {
    *fatorial = *fatorial * contador;
    contador = contador + 1;
  }
  
  return 0;
}
