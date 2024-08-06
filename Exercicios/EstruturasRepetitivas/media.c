#include <stdio.h>

int main(void) {
    int cont = 0;
    int numero, qtdNegativos, qtdPositivos, soma, qtd;
    float media;

    qtdNegativos = 0;
    qtdPositivos = 0;
    soma = 0;

    printf("Quantos valores vocês deseja calcular a media? ");
    scanf("%d", &qtd);
    while (qtd < 0){
        printf("Valor inválido! Digite novamente: ");
        scanf("%d", &qtd);
    }

    do {
    printf("Digite um numero");
    scanf("%d", &numero);
    if (numero >= 0){
        qtdPositivos++;
    } else{
        qtdNegativos++;
    }
    soma = soma + numero;
    cont++;
    } while (cont < qtd);

    media = soma / qtd;
    printf("Resultados: ");
    printf("Media %f", media);
    printf("Quantidade positivos %d", qtdPositivos);
    printf("Quantidade negativos %d", qtdNegativos);

    return 0; 
}
