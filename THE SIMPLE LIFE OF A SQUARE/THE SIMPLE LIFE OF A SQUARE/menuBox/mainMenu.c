#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <stdbool.h>
#include "mainMenu.h"
#include "gameCurrent.c"

void mainMenuu()
{
    system("cls");
    linhaCol(27, 50);
    printf("ATENCAO, POR EM TELA PRENCHIDA!!!");
    linhaCol(30, 50);
    printf("Clique para continuar...");
    getch();

    system("cls");
    supermegasaltodelinha(30);
    loading();
    system("cls");
    supermegasaltodelinha(10);
    printf(R"EOF(
                                                  ________  ________   _____ ______  _______  __    ______   __    ________________   ____  ______   ___       _____ ____  __  _____    ____  ______
                                                 /_  __/ / / / ____/  / ___//  _/  |/  / __ \/ /   / ____/  / /   /  _/ ____/ ____/  / __ \/ ____/  /   |     / ___// __ \/ / / /   |  / __ \/ ____/
                                                  / / / /_/ / __/     \__ \ / // /|_/ / /_/ / /   / __/    / /    / // /_  / __/    / / / / /_     / /| |     \__ \/ / / / / / / /| | / /_/ / __/
                                                 / / / __  / /___    ___/ // // /  / / ____/ /___/ /___   / /____/ // __/ / /___   / /_/ / __/    / ___ |    ___/ / /_/ / /_/ / ___ |/ _, _/ /___
                                                /_/ /_/ /_/_____/   /____/___/_/  /_/_/   /_____/_____/  /_____/___/_/   /_____/   \____/_/      /_/  |_|   /____/\___\_\____/_/  |_/_/ |_/_____/
    )EOF");

 supermegasaltodelinha(10);
 boxmenuu();

}

void loading() {

    int i;
    supermegaTAB(14); printf("Loading...\n\n");
    for (i = 10; i <= 100; i += 10) {
        supermegaTAB(14); printf("[");
        int j;
        for (j = 0; j < i / 10; j++) {
            printf("=");
        }
        printf(">");
        for (j = i / 10 + 1; j <= 10; j++) {
            printf(" ");
        }
        printf("] %d%%", i);
        fflush(stdout);  // Limpa o buffer de sa�da
        usleep(500000);  // Espera 500ms (0.5 segundos)
        printf("\r");    // Volta ao in�cio da linha
    }
    printf("\n");
}

void boxmenuu()
{
    int op,nItens;
    char lista[3][50] = {"Jogar","Reiniciar","Sair"};
    nItens = sizeof(lista) / sizeof(lista[0]); //Saber nro de elementos de lista


    setlocale(LC_ALL, ""); // Definir a localidade padrão


    while(true){
       op = optionsCenter(10,50,nItens,lista); //Posicao do painel vertical e horizontal mente | Numero de intens e a lista dos itens

       if(op == 1){
         system("cls");
            perguntar();
       }
       else if(op == 2){
         system("cls");
         mainMenuu();
       }
       else if(op==3){
         linhaCol(50, 100);
         exit(0);
       }
   }
}

