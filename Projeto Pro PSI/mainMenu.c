#include "menuBox.c"
#include <unistd.h>

void name_game();
void supermegaTAB(int);
void supermegasaltodelinha(int);

void mainMenuu(){
  int op;

  supermegasaltodelinha(100);
  printf(R"EOF(
            ________  __    __  ________           _____   ______   __    __  _______   __    __  ________  __      __         ______   ________         ______          ______    ______   __    __   ______   _______   ________
           /        |/  |  /  |/        |         /     | /      \ /  |  /  |/       \ /  \  /  |/        |/  \    /  |       /      \ /        |       /      \        /      \  /      \ /  |  /  | /      \ /       \ /        |
          $$$$$$$$/ $$ |  $$ |$$$$$$$$/          $$$$$ |/$$$$$$  |$$ |  $$ |$$$$$$$  |$$  \ $$ |$$$$$$$$/ $$  \  /$$/       /$$$$$$  |$$$$$$$$/       /$$$$$$  |      /$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$  |$$$$$$$$/
             $$ |   $$ |__$$ |$$ |__                $$ |$$ |  $$ |$$ |  $$ |$$ |__$$ |$$$  \$$ |$$ |__     $$  \/$$/        $$ |  $$ |$$ |__          $$ |__$$ |      $$ \__$$/ $$ |  $$ |$$ |  $$ |$$ |__$$ |$$ |__$$ |$$ |__
             $$ |   $$    $$ |$$    |          __   $$ |$$ |  $$ |$$ |  $$ |$$    $$< $$$$  $$ |$$    |     $$  $$/         $$ |  $$ |$$    |         $$    $$ |      $$      \ $$ |  $$ |$$ |  $$ |$$    $$ |$$    $$< $$    |
             $$ |   $$$$$$$$ |$$$$$/          /  |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$ $$ $$ |$$$$$/       $$$$/          $$ |  $$ |$$$$$/          $$$$$$$$ |       $$$$$$  |$$ |_ $$ |$$ |  $$ |$$$$$$$$ |$$$$$$$  |$$$$$/
             $$ |   $$ |  $$ |$$ |_____       $$ \__$$ |$$ \__$$ |$$ \__$$ |$$ |  $$ |$$ |$$$$ |$$ |_____     $$ |          $$ \__$$ |$$ |            $$ |  $$ |      /  \__$$ |$$ / \$$ |$$ \__$$ |$$ |  $$ |$$ |  $$ |$$ |_____
             $$ |   $$ |  $$ |$$       |      $$    $$/ $$    $$/ $$    $$/ $$ |  $$ |$$ | $$$ |$$       |    $$ |          $$    $$/ $$ |            $$ |  $$ |      $$    $$/ $$ $$ $$< $$    $$/ $$ |  $$ |$$ |  $$ |$$       |
             $$/    $$/   $$/ $$$$$$$$/        $$$$$$/   $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$$$$$$$/     $$/            $$$$$$/  $$/             $$/   $$/        $$$$$$/   $$$$$$  | $$$$$$/  $$/   $$/ $$/   $$/ $$$$$$$$/
                                                                                                                                                                           $$$/
)EOF");

 printf("\n\n");
 supermegaTAB(11);
 printf("Clique em qualquer letra para continuar");
 getch();
 system("cls");

 supermegasaltodelinha(30);
 loading();

 boxmenuu();

}

void supermegaTAB(int nTAB){
for(int x=0;x<nTAB;x++){
    printf("\t");
  }
}

void supermegasaltodelinha(int nSaltos){
for(int x=0;x<nSaltos;x++){
    printf("\n");
  }
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
