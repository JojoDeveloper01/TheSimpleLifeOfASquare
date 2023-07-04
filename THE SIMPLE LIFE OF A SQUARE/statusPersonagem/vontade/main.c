#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <string.h>
#include <locale.h>
#include "box.h"

struct WC
{
    int mijo;
    int processo_de_fazer_coco;
} wc;

int main()
{
    setlocale(LC_ALL, "");

    int opcao, nItens;
    char lista[3][50]; // Array para armazenar o nome (8 letras + '\0')

    nItens = sizeof(lista) / sizeof(lista[0]);

    // Copy the string to lista
    strcpy(lista[0], "|||WC|||");
    strcpy(lista[1], "Mijar");
    strcpy(lista[2], "Coco");

    FILE *vontade;

    system("cls");

    vontade = fopen("../statusPersonagem/vontade.txt", "w");
    fprintf(vontade,"--VONTADE--");
    fclose(vontade);

    wc.mijo = 5;
    wc.processo_de_fazer_coco = 10;

    while (1)
    {
        opcao = optionsCenter(15,10, nItens, lista);

        if (opcao == 2)
        {
            system("cls");
            linhaCol(14, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
            printf("Preperando para mijar");
            for(int x=0; x<3; x++)
            {
                sleep(1);
                printf(".");
            }

            printf("\nSPACE varias vezes para dar a maxima potencia!!!");
            spacePUMBA();
            system("cls");
            linhaCol(14, 57);
            Sleep(2);
            printf("O seu mijo foi um sucesso!");
            getch();

            vontade = fopen("../statusPersonagem/vontade.txt", "a");

            if (vontade == NULL)
            {
                linhaCol(14, 70);
                printf("Erro ao abrir o arquivo.\n");
                exit(0);
            }
            // Escrever informa��es no arquivo
            fprintf(vontade,"\nMijo:\n%i",wc.mijo);
            // Fechar o arquivo
            fclose(vontade);
            break;
        }
        else if (opcao == 3)
        {
            system("cls");
            linhaCol(14, 57); //1a -> Posicao vertical | 2a -> Posicao horizontal
            printf("Preperando para fazer cocozinho");
            for(int x=0; x<3; x++)
            {
                sleep(1);
                printf(".");
            }

            printf("\nSPACE varias vezes para dar a maxima potencia!!!");
            bolinha();
            system("cls");
            linhaCol(14, 57);
            Sleep(2);
            printf("O seu super coco foi um sucesso!");
            getch();

            vontade = fopen("../statusPersonagem/vontade.txt", "a");

            if (vontade == NULL)
            {
                linhaCol(14, 70);
                printf("Erro ao abrir o arquivo.\n");
                exit(0);
            }
            // Escrever informa��es no arquivo
            fprintf(vontade,"\nCoco:\n%i",wc.processo_de_fazer_coco);
            // Fechar o arquivo
            fclose(vontade);
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

void spacePUMBA()
{

    printf(R"EOF(

                                      SSS  PPPP  AA   CCC EEEE
                                     S     P   PA  A C    E
                                      SSS  PPPP AAAA C    EEE
                                         S P    A  A C    E
                                     SSSS  P    A  A  CCC EEEE


                )EOF");

    getch();
    system("cls");
    printf(R"EOF(

                                          SSS  PPPP  AA   CCC EEEE
                                         S     P   PA  A C    E
                                          SSS  PPPP AAAA C    EEE
                                             S P    A  A C    E
                                         SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(

                                  SSS  PPPP  AA   CCC EEEE
                                 S     P   PA  A C    E
                                  SSS  PPPP AAAA C    EEE
                                     S P    A  A C    E
                                 SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(

                                          SSS  PPPP  AA   CCC EEEE
                                         S     P   PA  A C    E
                                          SSS  PPPP AAAA C    EEE
                                             S P    A  A C    E
                                         SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                  SSS  PPPP  AA   CCC EEEE
                                                 S     P   PA  A C    E
                                                  SSS  PPPP AAAA C    EEE
                                                     S P    A  A C    E
                                                 SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                                  SSS  PPPP  AA   CCC EEEE
                                                                 S     P   PA  A C    E
                                                                  SSS  PPPP AAAA C    EEE
                                                                     S P    A  A C    E
                                                                 SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                      SSS  PPPP  AA   CCC EEEE
                                                     S     P   PA  A C    E
                                                      SSS  PPPP AAAA C    EEE
                                                         S P    A  A C    E
                                                     SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                          SSS  PPPP  AA   CCC EEEE
                                         S     P   PA  A C    E
                                          SSS  PPPP AAAA C    EEE
                                             S P    A  A C    E
                                         SSSS  P    A  A  CCC EEEE

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                              SSS  PPPP  AA   CCC EEEE
                                                             S     P   PA  A C    E
                                                              SSS  PPPP AAAA C    EEE
                                                                 S P    A  A C    E
                                                             SSSS  P    A  A  CCC EEEE

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                                          SSS  PPPP  AA   CCC EEEE
                                                                         S     P   PA  A C    E
                                                                          SSS  PPPP AAAA C    EEE
                                                                             S P    A  A C    E
                                                                         SSSS  P    A  A  CCC EEEE


                )EOF");
    getch();

}

void bolinha(){

printf(R"EOF(
      __    _       ___             _      _   _   ___        __    _
      )_)  / )  )    )   )\ )  )_) )_)    / ` )_)   )   )\ )  ) )  / )
     /__) (_/  (__ _(_  (  (  ( ( / /    (_  / /  _(_  (  (  /_/  (_/

                )EOF");

    getch();
    system("cls");
    printf(R"EOF(

                      __    _       ___             _      _   _   ___        __    _
                      )_)  / )  )    )   )\ )  )_) )_)    / ` )_)   )   )\ )  ) )  / )
                     /__) (_/  (__ _(_  (  (  ( ( / /    (_  / /  _(_  (  (  /_/  (_/
                )EOF");
    getch();
    system("cls");
    printf(R"EOF(

                                      __  __       _   __
                                     (_   )_)  )  )_) (_   )_) ( ( (
                                     __) /    (__/ /  __) ( (  o o o

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                   _     ___ __   _     __    _       ___             _
                                                  / ) / / )  )_) )_)    )_)  / )  )    )   )\ )  )_) )_)
                                                 (_/ (_/ (  / \ / /    /__) (_/  (__ _(_  (  (  ( ( / /

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                              __    _       ___             _      _   _   ___        __    _
                              )_)  / )  )    )   )\ )  )_) )_)    / ` )_)   )   )\ )  ) )  / )
                             /__) (_/  (__ _(_  (  (  ( ( / /    (_  / /  _(_  (  (  /_/  (_/
                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                          __  __       _   __
                                         (_   )_)  )  )_) (_   )_) ( ( (
                                         __) /    (__/ /  __) ( (  o o o

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                              __    _       _      _  __   _         __  ___
                                                              )_)  / )  )  )_)    / _ )_) )_)  )\ )  ) ) )_  ( ( ( ( ( (
                                                             /__) (_/  (__/ /    (__(/ \ / /  (  (  /_/ (__  o o o o o o


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                          __    _       _      _  __   _         __  ___     _   _   ___        __    _
                          )_)  / )  )  )_)    / _ )_) )_)  )\ )  ) ) )_     / ` )_)   )   )\ )  ) )  / ) ( ( ( ( ( (
                         /__) (_/  (__/ /    (__(/ \ / /  (  (  /_/ (__    (_  / /  _(_  (  (  /_/  (_/  o o o o o o

                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                         __      __  ___ __         ___   _   _     __  __       _   __
                                        (_  / /  )_) )_  )_)   )\/) )_   / _ )_)   (_   )_)  )  )_) (_   )_) ( ( (
                                        __)(_/  /   (__ / \   (  ( (__  (__(/ /    __) /    (__/ /  __) ( (  o o o


                )EOF");
    getch();
    system("cls");
    printf(R"EOF(
                                                         BBBB   OOO  M   M BBBB  AA      AA  TTTTTT  OOO  M   M III  CCC AA
                                                         B   B O   O MM MM B   BA  A    A  A   TT   O   O MM MM  I  C   A  A
                                                         BBBB  O   O M M M BBBB AAAA    AAAA   TT   O   O M M M  I  C   AAAA
                                                         B   B O   O M   M B   BA  A    A  A   TT   O   O M   M  I  C   A  A
                                                         BBBB   OOO  M   M BBBB A  A    A  A   TT    OOO  M   M III  CCCA  A


                )EOF");
    getch();

}












