#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <string.h>
#include "modoDeVida.h"


void indigente()
{
    welcome();
    movePlayer();

}

void welcome()
{
    setlocale(LC_ALL, "Portuguese");

    system("cls");
    linhaCol(30, 81);
    printf("Estás prestes a embarcar numa jornada sombria e cruel, adentrando a vida de um desafortunado ser humano. ");
    getch();
    printf("\n\t\t\t\t\t\t\t\t\t\tPrepara-te para testemunhar a implacável realidade que espera pelo nosso protagonista, desde o momento do seu nascimento até a sua morte.");
    getch();

    system("cls");
    linhaCol(30, 81);
    printf("Nasces-te numa aldeia chamada Babilónia, imerso em extrema pobreza.");
    getch();
    system("cls");
    linhaCol(31, 81);
    printf("Sendo órfão, terás de sobreviver por conta própria, sem saber a tua idade e sem memórias além do teu nome %s", per.nome);
    linhaCol(31, 81);
    printf("\n\n\n\n\t\t\t\t\t\t\t\t\t\tQUE O JOGO COMECE...");
    getch();
}

void movePlayer()
{
    int x = 110;
    int y = 50;
    char tecla;


    while (1)
    {
        system("cls");
        space();
        // Imprime o asterisco na posição atual (x, y)
        posY(y);
        posX(x);
        printf("********");

        posY(1);
        posX(x);
        printf("********");

        posY(1);
        posX(x);
        printf("********");

        posY(1);
        posX(x);
        printf("********");

        // Captura a tecla pressionada
        tecla = getch();

        // Move o asterisco de acordo com a tecla pressionada
        switch (tecla)
        {
        case 'w':
            y -= 3;
            break;
        case 'a':
            x -= 5;
            break;
        case 'd':
            x += 5;
            break;
        case 'q':
            break; // Sai do programa se pressionar 'q'
        }
    }

}

void posX(int x)
{
    for (int i = 0; i < x; i++)
    {
        printf(" ");
    }
}

void posY(int y)
{
    for (int i = 0; i < y; i++)
    {
        printf("\n");
    }
}

void space()
{

    /*printf("/"
          "/"
         "/"
        "/"
       "/"
      "/"
     "/"
    "/");*/

    int X = 110;
    posY(30);
    for(int x=0; x<10; x++)
    {
        posX(X);
        printf("/\n");
        X--;
        break;
    }


}
