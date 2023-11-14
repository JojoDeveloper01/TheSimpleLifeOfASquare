#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <string.h>
#include <locale.h>
#include "box.h"

struct cozinha
{
    int banana;
    int carne_de_porco;
    int sandwiche;
    int batata;
} coz;

int main()
{
    coz.banana=2;
    coz.carne_de_porco = 14;
    coz.sandwiche = 15;
    coz.batata = 1;

    setlocale(LC_ALL, "");

    int opcao, nItens;
    char lista[6][50]; // Array para armazenar o nome (8 letras + '\0')

    nItens = sizeof(lista) / sizeof(lista[0]);

    // Copy the string to lista
    strcpy(lista[0], "|||COZINHA|||");
    strcpy(lista[1], "Possiveis escolhas: ");
    strcpy(lista[2], "Banana");
    strcpy(lista[3], "Batata cozida");
    strcpy(lista[4], "carne de porco");
    strcpy(lista[5], "Sandwiche");

    FILE *comida;

    system("cls");

    comida = fopen("../statusPersonagem/comida.txt", "w");
    fprintf(comida,"--COZINHA--");
    fclose(comida);

    while (1)
    {
        opcao = optionsCenter(15,10, nItens, lista);

            if(opcao==3)
            {
                system("cls");
                linhaCol(14, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
                printf("Banana comida com sucesso.");
                getch();

                comida = fopen("../statusPersonagem/comida.txt", "a");

                if (comida == NULL)
                {
                    linhaCol(14, 70);
                    printf("Erro ao abrir o arquivo.\n");
                    exit(0);
                }

                // Escrever informa��es no arquivo
                fprintf(comida,"\nBanana:\n%i",coz.banana);
                // Fechar o arquivo
                fclose(comida);
                break;
        }
        else if (opcao == 4)
        {
                system("cls");
                linhaCol(12, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
                printf("Batata cozida comida com sucesso.");
                getch();

                comida = fopen("../statusPersonagem/comida.txt", "a");

                if (comida == NULL)
                {
                    linhaCol(14, 70);
                    printf("Erro ao abrir o arquivo.\n");
                    exit(0);
                }

                // Escrever informa��es no arquivo
                fprintf(comida,"\nBatata cozida:\n%i",coz.batata);
                // Fechar o arquivo
                fclose(comida);
                 break;
        }
        else if (opcao == 5)
        {
                system("cls");
                linhaCol(12, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
                printf("Carne de porco comida com sucesso.");
                getch();

                comida = fopen("../statusPersonagem/comida.txt", "a");

                if (comida == NULL)
                {
                    linhaCol(14, 70);
                    printf("Erro ao abrir o arquivo.\n");
                    exit(0);
                }

                // Escrever informa��es no arquivo
                fprintf(comida,"\nCarne de porco:\n%i",coz.carne_de_porco);
                // Fechar o arquivo
                fclose(comida);
                 break;
        }
        else if (opcao == 6)
        {
                system("cls");
                linhaCol(12, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
                printf("Sandwiche comido com sucesso.");
                getch();

                comida = fopen("../statusPersonagem/comida.txt", "a");

                if (comida == NULL)
                {
                    linhaCol(14, 70);
                    printf("Erro ao abrir o arquivo.\n");
                    exit(0);
                }

                // Escrever informa��es no arquivo
                fprintf(comida,"\nSandwiche:\n%i",coz.sandwiche);
                // Fechar o arquivo
                fclose(comida);
                break;
        }
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
















