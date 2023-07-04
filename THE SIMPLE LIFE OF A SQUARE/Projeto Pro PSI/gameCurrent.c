#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <stdbool.h>
#include <string.h>
#include "gameCurrent.h"


void perguntar()
{
    namePlayer(3);
    sexo(4);
    modoVida(5);
}

void namePlayer(int nLine)
{
    setlocale(LC_ALL, "portuguese");

    int opcao, nItens;
    char lista[nLine][50]; // Array para armazenar o nome (8 letras + '\0')

    nItens = sizeof(lista) / sizeof(lista[0]);

    // Copy the string to lista
    strcpy(lista[0], "Nome: ");
    strcpy(lista[1], " ");
    strcpy(lista[2], "Voltar");

    FILE *dadosP;

    system("cls");
    while (true)
    {
        opcao = optionsCenter(15,10, nItens, lista);

        if (opcao == 2)
        {
            linhaCol(29, 113); //1a -> Posicao vertical | 2a -> Posicao horizontal
            scanf("%s", per.nome);

            dadosP = fopen("dadosPersonagem.txt", "w");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("Erro ao abrir o arquivo.\n");
                exit(0);
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n\n|||>>Informação Personagens<<|||\n\n  -> Nome: %s",per.nome);
            // Fechar o arquivo
            fclose(dadosP);

            sexo(4); //Avanzar
        }


        else if(opcao == 3)
        {
            mainMenuu();
        }
    }

}

void sexo(int nLine)
{
    int opcao, nItens;
    char lista[nLine][50];
    nItens = sizeof(lista) / sizeof(lista[0]);

    setlocale(LC_ALL, " ");

    // Copy the strings to lista
    strcpy(lista[0], "SEXO: ");
    strcpy(lista[1], "Homem");
    strcpy(lista[2], "Mulher");
    strcpy(lista[3], "Voltar");

    FILE *dadosP;

    system("cls");
    while (true)
    {
        opcao = optionsCenter(10, 50, nItens, lista);

        if (opcao == 2)
        {
            per.sexo = 1; // homem

            dadosP = fopen("dadosPersonagem.txt", "a");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("\nErro ao abrir o arquivo.");
                exit(0);
            }

            fprintf(dadosP,"\n  -> Sexo: Homem");
            // Fechar o arquivo
            fclose(dadosP);

            modoVida(5);
        }
        else if (opcao == 3)
        {
            per.sexo = 2; // mulher

            dadosP = fopen("dadosPersonagem.txt", "a");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("\nErro ao abrir o arquivo.");
                exit(0);
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n  -> Sexo: Mulher");
            // Fechar o arquivo
            fclose(dadosP);

            modoVida(5);
        }
        else if (opcao == 4)
        {
            mainMenuu();
        }
    }
}

//Modo de vida: indigente, alta vida, Guerrab
void modoVida(int nLine)
{
    int opcao, nItens;
    char lista[nLine][50];
    nItens = sizeof(lista) / sizeof(lista[0]);

    setlocale(LC_ALL, " ");

    // Copy the strings to lista
    strcpy(lista[0], "MODO DE VIDA: ");
    strcpy(lista[1], "Normal");
    strcpy(lista[2], "Alta Vida");
    strcpy(lista[3], "Guerra");
    strcpy(lista[4], "Voltar");

    FILE *dadosP;

    system("cls");
    while (true)
    {
        opcao = optionsCenter(50, 10, nItens, lista);

        if (opcao == 2)
        {
            per.indigente=1;

            dadosP = fopen("dadosPersonagem.txt", "a");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("\nErro ao abrir o arquivo.");
                exit(0);
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n  -> Modo de Vida: Normal");
            // Fechar o arquivo
            fclose(dadosP);
            comeco();

            system("python ..//Jogar//jogar.py");

              mainMenuu();
        }
        else if (opcao == 3)
        {
            linhaCol(40, 114);
            printf("Proximamente...");

            //altaVida();
        }
        else if (opcao == 4)
        {
            linhaCol(40, 114);
            printf("Proximamente...");
            //guerra();

        }
        else if (opcao == 5)
        {
            mainMenuu();
        }
    }
}

void comeco(){
  system("cls");
  linhaCol(30, 100);
  printf("PRONTO PARA VIVER A SIMPLES VIDA DE UM CUADRADO?");
  getch();
  system("cls");
  linhaCol(30, 100);
  printf("Nem precisas de dizer nada, comecemos!");
  linhaCol(40, 100);
  system("pause");



}



