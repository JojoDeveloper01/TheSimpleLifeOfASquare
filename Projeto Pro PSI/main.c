#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <stdbool.h>

void linhaCol(int lin, int col);
void box(int lin1, int col1, int lin2, int col2);
int menu(int lin1, int col1, int qtd, char lista[3][40]);
void textColor(int letras, int fundo);


  //COR DA LETRA
  enum{_BLACK,                 //0
       _BLUE,                  //1
       _GREEN,                 //2
       _CYAN,                  //3
       _RED,                   //4
       _MAGENTA,               //5
       _BROWN,                 //6
       _LIGHTGRAY,             //7
       _DARKGRAY,              //8
       _LIGHTBLUE,             //9
       _LIGHTGREEN,            //10
       _LIGHTCYAN,             //11
       _LIGHTRED,              //12
       _LIGHTMAGENTA,          //13
       _YELLOW,                //14
       _WHITE                  //15

       };

enum {
    __BLACK = 0,
    __BLUE = 4,
    __GREEN = 32,
    __CYAN = 48,
    __RED = 64,
    __MAGENTA = 80,
    __BROWN = 96,
    __LIGHTGRAY = 112,
    __DARKGRAY = 128,
    __LIGHTBLUE = 144,
    __LIGHTGREEN = 160,
    __LIGHTCYAN = 176,
    __LIGHTRED = 192,
    __LIGHTMAGENTA = 208,
    __ORANGE = 214,
    __YELLOW = 224,
    __WHITE = 255
};

 //  Definir as cores do texto e do fundo no console
void textColor(int letra, int fundo){
     SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), letra + fundo);
     }

//Posicionar o cursor do console em uma determinada linha e coluna
void linhaCol(int lin, int col){
     SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),(COORD){col-1,lin-1});// coorddenada na tela

     //funcao para deixar o cursor invisivel
     HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
     CONSOLE_CURSOR_INFO info;
     info.dwSize = 100;
     info.bVisible = FALSE;
     SetConsoleCursorInfo(consoleHandle, &info);
}

// Desenha uma caixa retangular no console usando caracteres ASCII para criar os cantos, linhas horizontais e verticais
void box(int lin1, int col1, int lin2, int col2){
     int i,j , tamlin, tamcol;

     //achar o tamanho do box
     tamlin = lin2 - lin1;
     tamcol = col2 - col1;

     //Monta o Box

     for (i=col1; i<=col2; i++){ // linhas
         linhaCol(lin1,i);
         printf("%c",196);  //Linha Acima
         linhaCol(lin2,i);
         printf("%c",196); //Linha Abaixo
         }

     for (i=lin1; i<=lin2; i++){ //colunas
         linhaCol(i,col1);
         printf("%c",179); //Linha esquerda
         linhaCol(i,col2);
         printf("%c",179); //Linha direita
         }

     for (i=lin1+1;i<lin2;i++){
         for(j=col1+1;j<col2;j++){
            linhaCol(i,j);printf(" "); //Fundo
          }
         }

     //Cantos
     linhaCol(lin1,col1);
     printf("%c",218); //acima esquerdo
     linhaCol(lin1,col2);
     printf("%c",191); // acima direito
     linhaCol(lin2,col1);
     printf("%c",192); // abaixo esquerdo
     linhaCol(lin2,col2);
     printf("%c",217); //abaixo direito

     }


int menu(int lin1, int col1, int qtd, char lista[3][40]){
     int op=1, lin2, col2, linha,i,tamMaxItem, tecla;

     //calcula as coordenadas
     tamMaxItem = strlen(lista[0]);
     //tamanho maximo do item
     for(i=1; i<qtd;i++){
       if(strlen(lista[i])>tamMaxItem){
          tamMaxItem = strlen(lista[i]);
       }
     }
     lin2 = lin1+(qtd*2+2);
     col2 = col1+tamMaxItem+4;

     //Monta Tela
     textColor(_RED, __BLUE); //Fundo da tela
     setlocale(LC_ALL,"C");
     box(lin1,col1,lin2,col2);
     setlocale(LC_ALL,"");
     //lado das opcoes

     while(1){
        linha=lin1+2;
        for(i=0;i<qtd;i++){
           if(i+1==op)textColor(_WHITE, __BLACK);
           else textColor(_WHITE, __BLACK);
        linhaCol(linha,col1+2);
        printf("%s",lista[i]);
        linha +=2;
        }

       //Aguarda tecla
       linhaCol(1,1);
       tecla= getch();
       linhaCol(22,1);
       //printf(" tecla:  %d   ",tecla);
       //Op��o
       if(tecla==27){ //ESC
       op=0; break;
       }
       else if(tecla==13){ //ENTER
       break;
       }
       //Seta para cima
       else if(tecla==72){ //se possivel seleciona o item anterior - seta para cima
            if(op>1)op--;  // se opao for maior que 1, pode voltar

       }
       else if(tecla==80 ){        //seta para baixo
            if (op<qtd)op++;                //Se opao for menor que quantidade de itens, posso avan�ar


       //printf("tecla: %d ",op);
       }
     }
     return op;
}

int main()
{
    int op,nItens;
    char lista[3][40]={"Carregar Jogo", "Novo Jogo", "Sair"};
    nItens = sizeof(lista) / sizeof(lista[0]); //Saber nro de elementos de lista

    setlocale(LC_ALL,"");

    while(true){
       op = menu(10,50,nItens,lista); //Posicao do painel vertical e horizontalmente | Numero de intens e a lista dos itens

       if (op==0){
       break;
       }

        linhaCol(1,1);
        textColor(_BLACK, __WHITE);
        printf("\nEscolheu a opção %i", op);

    }

  textColor(BLACK, __RED);
  linhaCol(24,1);
  printf("");

  return 0;
}
