#ifndef GAMECURRENT_H
#define GAMECURRENT_H

int nLine;
void linhaColuna(int linha, int coluna);
void caixa(int linha1, int coluna1, int linha2, int coluna2);
int optionsCenter(int linha1, int coluna1, int quantidade, char lista[nLine][50]);
void corTexto(int letras, int fundo);

struct personagem
{
    int sexo,indigente,altaV,guerra;
    char nome[10];
} per;

#endif
