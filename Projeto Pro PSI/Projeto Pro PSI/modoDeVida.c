#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <locale.h>
#include <string.h>
#include "gameCurrent.h"

void indigente(){

  system("cls");
  linhaCol(30, 81);
  printf("Você nasce em uma pequena cidade chamada Tundam, cercada por paisagens exuberantes."
         "\n\t\t\t\t\t\t\t\t\t\tSeus pais estão cheios de infelicidade e odio ao verem seu rosto do seu filho não desejado."
         "\n\t\t\t\t\t\t\t\t\t\tEles dão a você um nome odiado por muitos... %s, que significa 'demonio' na lingua antiga deles.", per.nome);

  printf("\n\n\t\t\t\t\t\t\t\t\t\tClicar para cotinuar...");
  getch();

}
