#include <stdio.h>

float chico = 1.50;
float crescimentoChico = 0.02;

float ze = 1.10;
float crescimentoZe = 0.03;

int anosParaZeSerMaior() {
    int anos = 0;
    while (ze <= chico) {
        chico += crescimentoChico;
        ze += crescimentoZe;
        anos++;
    }
    return anos;
}

int main() {
    printf("Anos necessarios para Ze ser maior que Chico: %d\n", anosParaZeSerMaior());
    return 0;
}
