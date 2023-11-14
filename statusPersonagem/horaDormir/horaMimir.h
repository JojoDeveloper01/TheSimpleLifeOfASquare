#ifndef BOX_H
#define BOX_H

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <string.h>

int nLine;

enum
{
    _BLACK,
    _BLUE,
    _GREEN,
    _CYAN,
    _RED,
    _MAGENTA,
    _BROWN,
    _LIGHTGRAY,
    _DARKGRAY,
    _LIGHTBLUE,
    _LIGHTGREEN,
    _LIGHTCYAN,
    _LIGHTRED,
    _LIGHTMAGENTA,
    _YELLOW,
    _WHITE
};

enum
{
    BG_BLACK = 0,
    BG_BLUE = 16,
    BG_GREEN = 32,
    BG_CYAN = 48,
    BG_RED = 64,
    BG_MAGENTA = 80,
    BG_BROWN = 96,
    BG_LIGHTGRAY = 112,
    BG_DARKGRAY = 128,
    BG_LIGHTBLUE = 144,
    BG_LIGHTGREEN = 160,
    BG_LIGHTCYAN = 176,
    BG_LIGHTRED = 192,
    BG_LIGHTMAGENTA = 208,
    BG_YELLOW = 224,
    BG_WHITE = 240
};

//  Definir as cores do texto e do fundo no console
void textColor(int letra, int fundo)
    {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), letra + fundo);
}

//Posicionar o cursor do console em uma determinada linha e coluna
void linhaCol(int lin, int col)
{
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),(COORD)
    {
        col -1,lin -1
    });// coorddenada na tela

    //funcao para deixar o cursor invisivel
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = FALSE;
    SetConsoleCursorInfo(consoleHandle, &info);
}

// Desenha uma caixa retangular no console usando caracteres ASCII para criar os cantos, linhas horizontais e verticais
void boox(int lin1, int col1, int lin2, int col2) //variaveos que representam as coordenadas das linhas e colunas que delimitam o retângulo
{
    int i,j;

    //Monta o Box

    for (i=col1; i<=col2; i++)  // Desenhar as linhas superiores e inferiores do retângulo
    {
        linhaCol(lin1,i); //posicionar o cursor na posição correta
        printf("%c",196);  //Linha Acima
        linhaCol(lin2,i); //posicionar o cursor na posição correta
        printf("%c",196); //Linha Abaixo
    }

    for (i=lin1; i<=lin2; i++)  //Desenhar as linhas laterais esquerda e direita do retângulo
    {
        linhaCol(i,col1);//posicionar o cursor na posição correta
        printf("%c",179); //Linha esquerda
        linhaCol(i,col2);//posicionar o cursor na posição correta
        printf("%c",179); //Linha direita
    }

    for (i=lin1+1; i<lin2; i++) //Preencher o interior do retângulo com espaços vazios
    {
        for(j=col1+1; j<col2; j++)
        {
            linhaCol(i,j);
            printf(" "); //Fundo
        }
    }
    /*percorre as linhas desde lin1 + 1 até lin2 - 1 e, para cada linha,
     percorre as colunas desde col1 + 1 até col2 - 1. A função linhaCol
     é chamada para posicionar o cursor na posição correta, e em seguida é impresso um espaço vazio*/

    //Desenhar cantos
    linhaCol(lin1,col1);
    printf("%c",218); //acima esquerdo
    linhaCol(lin1,col2);
    printf("%c",191); // acima direito
    linhaCol(lin2,col1);
    printf("%c",192); // abaixo esquerdo
    linhaCol(lin2,col2);
    printf("%c",217); //abaixo direito

}

int optionsCenter(int lin1, int col1, int qtd, char lista[nLine][50])
{
    int op=1, lin2, col2, linha,i,tamMaxItem, tecla;
    float margem_vertical = 2; //posicao vertical do texto da boox
    int margem_horizontal = 13; //posicao horizontal do texto da boox

    //calcula as coordenadas
    tamMaxItem = strlen(lista[0]); // tamanho do primeiro item da lista


    //tamanho maximo do item
    /*verifica o tamanho de todos os itens da lista e atualiza
     o valor de tamMaxItem se algum item tiver um tamanho maior.*/
    for(i=1; i<qtd; i++)
    {
        if(strlen(lista[i])>tamMaxItem)
        {
            tamMaxItem = strlen(lista[i]);
        }
    }

    // Defina as coordenadas personalizadas para posicionar o boox do menu
    lin1 = 10;  // Posição vertical do início do boox
    col1 = 40;  // Posição horizontal do início do boox
    lin2 = lin1 + (qtd * 1 + 6);  // Tamanho vertical do boox
    col2 = col1 + tamMaxItem + 25; // Tamanho horizontal do boox

    //Montar Tela
    textColor(_WHITE, BG_BLACK); //Cor da linha do fundo da tela e do funcdo da tela
    setlocale(LC_ALL,"C");
    boox(lin1,col1,lin2,col2); //chama a função boox para desenhar o retângulo do menu
    setlocale(LC_ALL,""); //restaura a localidade padrão
    //lado das opcoes

    while(1) //CICLO INFINITO
    {
        linha = lin1 + margem_vertical;
        for(i=0; i<qtd; i++)
        {
            if(i+1==op)textColor(_BLACK, BG_WHITE);//Cor da letra do texto do meno e cor de fundo do menu
            else textColor(_WHITE, BG_BLACK);
            linhaCol(linha, col1 + margem_horizontal);
            printf("%s",lista[i]);
            linha +=2;
        }

        //Aguarda tecla
        linhaCol(1,1);

        tecla= getch();
        linhaCol(22,1);
        //printf(" tecla:  %d   ",tecla);
        //Op��o

        if(tecla==27)  //ESC
        {
            op=0;
            break;
        }
        else if(tecla==13)  //ENTER
        {
            break;
        }
        //Seta para cima
        else if(tecla==72)  //se possivel seleciona o item anterior - seta para cima
        {
            if(op>1)op--;  // se opao for maior que 1, pode voltar

        }
        else if(tecla==80 )    //seta para baixo
        {
            if (op<qtd)op++; //Se opcao for menor que quantidade de itens, posso avançar


        }
    }
    return op;//retorna o valor da opção selecionada pelo usuário
}

void supermegaTAB(int nTAB)
{
    for(int x=0; x<nTAB; x++)
    {
        printf("\t");
    }

}

void supermegasaltodelinha(int nSaltos)
{
    for(int x=0; x<nSaltos; x++)
    {
        printf("\n");
    }
}

#endif // BOX_H_INCLUDED

