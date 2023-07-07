#ifndef GAMECURRENT_H
#define GAMECURRENT_H

struct personagem
{
    int sexo,indigente,altaV,guerra;
    char nome[10];
} per;

int nLine;

void pergunta();
void namePlayer(int nLine2);
void sexo(int nLine3);
void modoVida(int nLine4);
void comeco();
//Funcoees Alheias
int optionsCenter(int,int,int,char [nLine][50]);
void mainMenuu();

#endif
