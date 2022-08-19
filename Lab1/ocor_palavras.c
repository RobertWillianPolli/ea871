/* Programa que verifica a quantidade de ocorrencias de uma palavra dentro 
 * de uma frase
 *
 * Exemplo de execução:
 *
 * Verifica a quantidade de ocorrências de uma substring dentro de uma string
 * Digite a palavra: ANATOMISTA ANA MARIANA GOSTA DE BANANA
 * Digite 1 sequência de caracteres buscada: ANA
 * A quantidade de ocorrências é 4
*/

#include <stdio.h>
#include <string.h>

int main() {
    char ocorre = 0;
    int m, n, i, j, numOcor=0;
    char frase[80], palavra[80];
    

    printf ("Verifica a quantidade de palavras\n");

    // le
    printf ("Digite a frase: ");
    scanf("%[^\n]%*c", frase);
 
    // leia a palavra buscada
    printf ("Digite a palavra buscada: ");
    scanf("%[^\n]%*c", palavra);

    // quantidade de letras em cada string
    m = strlen(frase);
    n = strlen(palavra);

    // conte a quantidade de ocorrências
    for (i=0; i <= m-n; i++) {
	    if (frase[i] == palavra[0]) {
	       ocorre = 1;
           for (j=1; j<n; j++) {
	           if (frase[i+j] != palavra[j]) {
		           ocorre = 0;
			   j++;
		           break;
	           }
	       }
	       numOcor = numOcor+ocorre;
	       if (ocorre) i=i+j-1;
        }
    }

    printf ("%s e %s tem, respectivamente, %d e %d letras\n", frase, palavra, m, n);
    printf ("A quantidade de ocorrencias de %s em %s eh %d\n", palavra, frase, numOcor);
    printf("Tamanhos:\n ocorre=%ld\n m=%ld\n n=%ld\n i=%ld\n j=%ld\n frase=%ld\n palavra=%ld\n", sizeof(ocorre), sizeof(m), sizeof(n), sizeof(i), sizeof(j), sizeof(frase), sizeof(palavra));
    return 0;
}

