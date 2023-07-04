#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <string.h>
#include "horaMimir.h"

struct dormir
{
    int horas;

} horasD;

int main()
{
    setlocale(LC_ALL, "portuguese");


    int opcao, nItens;
    char lista[2][50]; // Array para armazenar o nome (8 letras + '\0')


    nItens = sizeof(lista) / sizeof(lista[0]);


    // Copy the string to lista
    strcpy(lista[0], "Horas a dormir: ");
    strcpy(lista[1], " ");

    FILE *statusP;

    system("cls");
    while (1)
    {
        opcao = optionsCenter(15,10, nItens, lista);

        if (opcao == 2)
        {
            linhaCol(14, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
            scanf("%i", &horasD.horas);

            statusP = fopen("../statusPersonagem/horasSono.txt", "w");

            if (statusP == NULL)
            {
                linhaCol(14, 70);
                printf("Erro ao abrir o arquivo.\n");
                exit(0);
            }

            // Escrever informa��es no arquivo
            fprintf(statusP,"DORMIR: \nHoras a dormir:\n%i",horasD.horas);
            // Fechar o arquivo
            fclose(statusP);
        }
        break;
    }

    FILE *verificar;
    verificar = fopen("../statusPersonagem/verificarFecharEXE.txt", "w");

    if (verificar == NULL)
    {
        linhaCol(14, 70);
        printf("Erro ao abrir o arquivo.\n");
        exit(0);
    }
    fprintf(verificar,"6969");
    fclose(verificar);

    return 0;
}
