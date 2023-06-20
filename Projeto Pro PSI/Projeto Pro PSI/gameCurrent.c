#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <stdbool.h>
#include <string.h>  // Add this header for strcpy function
#include "modoDeVida.c"


enum
{
    __BLACK,
    __BLUE,
    __GREEN,
    __CYAN,
    __RED,
    __MAGENTA,
    __BROWN,
    __LIGHTGRAY,
    __DARKGRAY,
    __LIGHTBLUE,
    __LIGHTGREEN,
    __LIGHTCYAN,
    __LIGHTRED,
    __LIGHTMAGENTA,
    __YELLOW,
    __WHITE
};

enum
{
    BG__BLACK = 0,
    BG__BLUE = 16,
    BG__GREEN = 32,
    BG__CYAN = 48,
    BG__RED = 64,
    BG__MAGENTA = 80,
    BG__BROWN = 96,
    BG__LIGHTGRAY = 112,
    BG__DARKGRAY = 128,
    BG__LIGHTBLUE = 144,
    BG__LIGHTGREEN = 160,
    BG__LIGHTCYAN = 176,
    BG__LIGHTRED = 192,
    BG__LIGHTMAGENTA = 208,
    BG__YELLOW = 224,
    BG__WHITE = 240
};

int nLine;


void perguntar()
{
    name(3);
    sexo(4);
    modoVida(5);
}

void name(int nLine)
{
    setlocale(LC_ALL, "portuguese");

    int opcao, nItens;
    char lista[nLine][50]; // Array para armazenar o nome (8 letras + '\0')
    int contador = 0;  // Contador de letras digitadas

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
            linhaCol(30, 114); //1a -> Posicao vertical | 2a -> Posicao horizontal
            scanf("%s", per.nome);

            dadosP = fopen("dadosPersonagem.txt", "w");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("Erro ao abrir o arquivo.\n");
                return 0;
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
                return 0;
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
                return 0;
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

//Modo de vida: indigente, alta vida, Guerra

void modoVida(int nLine)
{
    int opcao, nItens;
    char lista[nLine][50];
    nItens = sizeof(lista) / sizeof(lista[0]);

    setlocale(LC_ALL, " ");

    // Copy the strings to lista
    strcpy(lista[0], "MODO DE VIDA: ");
    strcpy(lista[1], "Indigente");
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
                return 0;
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n  -> Modo de Vida: Indigente");
            // Fechar o arquivo
            fclose(dadosP);

            indigente(1);
        }
        else if (opcao == 3)
        {
            per.altaV = 1;
            dadosP = fopen("dadosPersonagem.txt", "a");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("\nErro ao abrir o arquivo.");
                return 0;
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n  -> Modo de Vida: Alta Vida");
            // Fechar o arquivo
            fclose(dadosP);

            //altaVida();
        }
        else if (opcao == 4)
        {
            per.guerra = 1;
            dadosP = fopen("dadosPersonagem.txt", "a");

            if (dadosP == NULL)
            {
                linhaCol(30, 114);
                printf("\nErro ao abrir o arquivo.");
                return 0;
            }

            // Escrever informações no arquivo
            fprintf(dadosP,"\n  -> Modo de Vida: Guerra");
            // Fechar o arquivo
            fclose(dadosP);

            //guerra();

        }
        else if (opcao == 5)
        {
            mainMenuu();
        }

    }

}

void supermegaTAB1(int nTAB)
{
    for(int x=0; x<nTAB; x++)
    {
        printf("\t");
    }

}
void supermegasaltodelinha1(int nSaltos)
{
    for(int x=0; x<nSaltos; x++)
    {
        printf("\n");
    }
}

// Definir as cores do texto e do fundo no console
void corTexto(int letra, int fundo)
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), letra + fundo);
}

//Posicionar o cursor do console em uma determinada linha e coluna
void linhaColuna(int linha, int coluna)
{
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),(COORD)
    {
        coluna -1,linha -1
    });// coorddenada na tela

    //funcao para deixar o cursor invisível
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = FALSE;
    SetConsoleCursorInfo(consoleHandle, &info);
}

// Desenha uma caixa retangular no console usando caracteres ASCII para criar os cantos, linhas horizontais e verticais
void caixa(int linha1, int coluna1, int linha2, int coluna2) //variáveis que representam as coordenadas das linhas e colunas que delimitam o retângulo
{
    int i,j ;

    //Monta o caixa

    for (i=coluna1; i<=coluna2; i++)  // Desenhar as linhas superiores e inferiores do retângulo
    {
        linhaColuna(linha1,i); //posicionar o cursor na posição correta
        printf("%c",196);  //Linha Acima
        linhaColuna(linha2,i); //posicionar o cursor na posição correta
        printf("%c",196); //Linha Abaixo
    }

    for (i=linha1; i<=linha2; i++)  //Desenhar as linhas laterais esquerda e direita do retângulo
    {
        linhaColuna(i,coluna1);//posicionar o cursor na posição correta
        printf("%c",179); //Linha esquerda
        linhaColuna(i,coluna2);//posicionar o cursor na posição correta
        printf("%c",179); //Linha direita
    }

    for (i=linha1+1; i<linha2; i++) //Preencher o interior do retângulo com espaços vazios
    {
        for(j=coluna1+1; j<coluna2; j++)
        {
            linhaColuna(i,j);
            printf(" "); //Fundo
        }
    }
    /*percorre as linhas desde linha1 + 1 até linha2 - 1 e, para cada linha,
     percorre as colunas desde coluna1 + 1 até coluna2 - 1. A função linhaColuna
     é chamada para posicionar o cursor na posição correta, e em seguida é impresso um espaço vazio*/

    //Desenhar cantos
    linhaColuna(linha1,coluna1);
    printf("%c",218); //acima esquerdo
    linhaColuna(linha1,coluna2);
    printf("%c",191); // acima direito
    linhaColuna(linha2,coluna1);
    printf("%c",192); // abaixo esquerdo
    linhaColuna(linha2,coluna2);
    printf("%c",217); //abaixo direito

}

int optionsCenter(int linha1, int coluna1, int quantidade, char lista[nLine][50])
{

    int opcao=1, linha2, coluna2, linha,i,tamMaxItem, tecla;
    float margem__vertical = 3; //posição vertical do texto da caixa
    int margem__horizontal = 15; //posição horizontal do texto da caixa

    //calcula as coordenadas
    tamMaxItem = strlen(lista[0]); // tamanho do primeiro item da lista


    //tamanho máximo do item
    /*verifica o tamanho de todos os itens da lista e atualiza
     o valor de tamMaxItem se algum item tiver um tamanho maior.*/
    for(i=1; i<quantidade; i++)
    {
        if(strlen(lista[i])>tamMaxItem)
        {
            tamMaxItem = strlen(lista[i]);
        }
    }

    // Defina as coordenadas personalizadas para posicionar o caixa do optionsCenter
    linha1 = 25;  // Posição vertical do início do caixa
    coluna1 = 100;  // Posição horizontal do início do caixa
    linha2 = linha1 + (quantidade * 1 + 8);  // Tamanho vertical do caixa
    coluna2 = coluna1 + tamMaxItem + 29; // Tamanho horizontal do caixa

    //Montar Tela
    corTexto(__WHITE, BG__BLACK); //Cor da linha do fundo da tela e do fundo da tela
    setlocale(LC_ALL,"C");
    caixa(linha1,coluna1,linha2,coluna2); //chama a função caixa para desenhar o retângulo do optionsCenter
    setlocale(LC_ALL,""); //restaura a localidade padrão
    //lado das opcoes

    while(1) //CICLO INFINITO
    {
        linha = linha1 + margem__vertical;
        for(i=0; i<quantidade; i++)
        {
            if(i+1==opcao)corTexto(__BLACK, BG__WHITE);//Cor da letra do texto do optionsCenter e cor de fundo do optionsCenter
            else corTexto(__WHITE, BG__BLACK);
            linhaColuna(linha, coluna1 + margem__horizontal);
            printf("%s",lista[i]);
            linha +=2;
        }

        //Aguarda tecla
        linhaColuna(1,1);

        tecla= getch();
        linhaColuna(22,1);
        //printf(" tecla:  %d   ",tecla);
        //Opção

        if(tecla==27)  //ESC
        {
            opcao=0;
            break;
        }
        else if(tecla==13)  //ENTER
        {
            break;
        }
        //Seta para cima
        else if(tecla==72)  //se possível seleciona o item anterior - seta para cima
        {
            if(opcao>1)opcao--;  // se opcao for maior que 1, pode voltar

        }
        else if(tecla==80 )    //seta para baixo
        {
            if (opcao<quantidade)opcao++; //Se opção for menor que quantidade de itens, posso avançar

        }
    }
    return opcao;//retorna o valor da opção selecionada pelo usuário

}

