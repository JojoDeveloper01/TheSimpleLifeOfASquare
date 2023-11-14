import pygame
import sys
import os
import random
import subprocess
import datetime
import time

# Dimensões do quadrado
QUADRADO_SIZE = 0

# Largura das faixas
FAIXAS_WIDTH = 0
# Dimensão das casas
CASAS_SIZE =200
# Dimensão das saídas das casas
SAIDA_WIDTH = 300
SAIDA_HEIGHT = 150

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREEN_DARK = (0, 100, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PURPLE_LIGTH = (180, 0, 180)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)
BROWN_DARK = (101, 67, 33)
BROWN_LIGHT = (150, 111, 51)

# Inicialização do Pygame
pygame.init()

# Configurações da tela cheia
fullscreen = pygame.FULLSCREEN

# Obtém as informações sobre a tela atual
screen_info = pygame.display.Info()

JANELA_WIDTH = screen_info.current_w
JANELA_HEIGHT = screen_info.current_h

square_x = JANELA_WIDTH // 2 - QUADRADO_SIZE // 2
square_y = JANELA_HEIGHT - (QUADRADO_SIZE + 160)
posAtualX = JANELA_WIDTH // 2 - SAIDA_WIDTH // 5
posAtualY = JANELA_HEIGHT - 130

posAcimax = 0
posAcimay = 0
verificarVoltar = False
posAbaixox = 0
posAbaixoy = 0
verificarVoltar2 = False

window = pygame.display.set_mode((JANELA_WIDTH, JANELA_HEIGHT), fullscreen)
pygame.display.set_caption("The Journey of a Square")

clock = pygame.time.Clock()

# Criar uma fonte de texto
def textoTam(tam):
  font = pygame.font.Font(None, tam)

# Nomes das casas
nomes_casas_esquerda = ["CASA", "CASA", "CASA", "CASA"]
nomes_casas_direita = ["CASA", "CASA", "CASA", "CASA"]
saidaCasa = ["F para sair"]
nomesRuas = ["R. piloto","R. ATM", "R. street", "R. do ladrao","R. do teu pai", "R. fixe", "R. do infinito"]

# Definir a velocidade de movimento
VELOCIDADE = 20  # Ajuste o valor para controlar a velocidade
enter_pressionado = False  # Variável global para controlar se a tecla Enter foi pressionada

vida = 10
fome = 10
stamina = 10
sono = 10
vontade = 10

tempo_inicial22= datetime.datetime.now()
tempo_inicial33= datetime.datetime.now()
tempo_inicial44= datetime.datetime.now()
tempo_inicial55= datetime.datetime.now()

tempo_inicial222= datetime.datetime.now()
tempo_inicial333= datetime.datetime.now()
tempo_inicial444= datetime.datetime.now()
tempo_inicial555= datetime.datetime.now()

def actualStatus():
    global vida, fome, stamina, sono, vontade,tempo_inicial22,tempo_inicial33,tempo_inicial44,tempo_inicial55,tempo_inicial222,tempo_inicial333,tempo_inicial444,tempo_inicial555
 
    tempo_atualFome22 = datetime.datetime.now()
    tempo_atualStamina44 = datetime.datetime.now()
    tempo_atualSono55 = datetime.datetime.now()

    # Calcular a diferença de tempo em segundos
    diferenca_tempo22 = (tempo_atualFome22 - tempo_inicial22).total_seconds()
    diferenca_tempo44 = (tempo_atualStamina44 - tempo_inicial44).total_seconds()
    diferenca_tempo55 = (tempo_atualSono55 - tempo_inicial55).total_seconds()


    #vida personagem
    if vida >= 10: vida = 10
    if vontade >= 10: vontade = 10

    if fome >= 10 and vida < 10: #FOME 22
        fome = 10
        if diferenca_tempo22 >= 10: #Cada 5s a vida aument 1 ponto
            vida += 1
            stamina += 1
            tempo_inicial22 = tempo_atualFome22

    if stamina >= 10 and vida < 10:#STAMINA 44
        stamina=10
        if diferenca_tempo44 >= 5:#Cada 5s a vida aument 1 ponto
            vida += 1
            tempo_inicial44 = tempo_atualStamina44
   
    if sono >= 10 and vida < 10: #SONO 55
        sono = 10
        if diferenca_tempo55 >= 5:#Cada 5s a vida aument 1 ponto
            vida += 1
            tempo_inicial55 = tempo_atualSono55

    #Quando ja estas tipo a morrer...

    tempo_atualFome222 = datetime.datetime.now()
    tempo_atualVontade333 = datetime.datetime.now()
    tempo_atualStamina444 = datetime.datetime.now()
    tempo_atualSono555 = datetime.datetime.now()

    # Calcular a diferença de tempo em segundos
    diferenca_tempo222 = (tempo_atualFome222 - tempo_inicial222).total_seconds()
    diferenca_tempo333 = (tempo_atualVontade333 - tempo_inicial333).total_seconds()
    diferenca_tempo444 = (tempo_atualStamina444 - tempo_inicial444).total_seconds()
    diferenca_tempo555 = (tempo_atualSono555 - tempo_inicial555).total_seconds()

    if vida <= 0: vida = 0 

    if fome <= 0:
        fome = 0 #fica sempre 0
        if diferenca_tempo222 >= 10: #Cada 5s a vida diminui 1 ponto
            vida -= 1 
            stamina -= 1
            sono += 1
            tempo_inicial222 = tempo_atualFome222

    if vontade <= 0: 
        vontade = 0 #fica sempre 0
        if diferenca_tempo333 >= 10: #Cada 5s a vida diminui 1 ponto
            vida -= 1
            tempo_inicial333 = tempo_atualVontade333

    if stamina <= 0:
        stamina = 0 #fica sempre 0
        if diferenca_tempo444 >= 10: #Cada 5s a vida diminui 1 ponto
            vida -= 1
            fome -=1
            sono -=1
            tempo_inicial444 = tempo_atualStamina444

    if sono <= 0: #ou seja, no maximo
        sono = 0 #fica sempre 0
        if diferenca_tempo555 >= 10: #Cada 5s a vida diminui 1 ponto
            vida -= 1
            stamina -= 1
            tempo_inicial555 = tempo_atualSono555

    if vida <= 0:
        morrer()

# Função para desenhar o fundo
def desenharFundo(cor):
    pygame.draw.rect(window, cor, (0, 0, JANELA_WIDTH, JANELA_HEIGHT))
# Função para desenhar as faixas
def desenharFaixas(cor,x,y,faixaWidth,faixaHeigth,x2,y2,faixaWidth2,faixaHeigth2):
    pygame.draw.rect(window, cor, (x, y, faixaWidth, faixaHeigth))
    pygame.draw.rect(window, cor, (x2, y2, faixaWidth2, faixaHeigth2))
# Função para desenhar uma casa
def desenharCasa(x, y, corHover, corPre, sel1,sel2):
    # Define a cor da casa com base na proximidade do quadrado
    cor_casa = corHover if abs(x - square_x) < sel1 and abs(y - square_y) < sel2 else corPre

    # Desenha a casa com bordas pretas
    pygame.draw.rect(window, BLACK, (x - 2, y - 2, CASAS_SIZE + 4, CASAS_SIZE + 4))  # Bordas
    pygame.draw.rect(window, cor_casa, (x, y, CASAS_SIZE, CASAS_SIZE))  # Quadrado
# Função para desenhar o texto das casas
def textoFixolasCasas(font  ,cor, x, y, nome):
    # Renderiza o texto com o nome da casa
    text = font.render(nome, True, cor)
    text_rect = text.get_rect(center=(x + CASAS_SIZE // 2, y + CASAS_SIZE // 2))
    window.blit(text, text_rect)
# Função para desenhar a saída
def desenharSaida(cor, posx, posy):
    pygame.draw.rect(window, cor, (posx, posy, SAIDA_WIDTH, SAIDA_HEIGHT))
# Função para desenhar o texto da saída
def textoFixolas(tamTexto,titulo,num,cor,posx, posy, tamWidth,tamHeight):
    font = pygame.font.Font(None, tamTexto)

    text = font.render(titulo[num], True, cor)
    text_rect = text.get_rect(center=(posx + tamWidth // 2, posy + tamHeight // 2))
    window.blit(text, text_rect)

# Função para desenhar o quadrado
def desenharQuadrado(corSquare, posAcx, posAcy):
    global vida, fome, stamina, sono, vontade

    if(vida>=10):vida=10
    if(fome>=10):fome=10
    if(stamina>=10):stamina=10
    if(sono>=10):sono=10
    if(vontade>=10):vontade=10

    if(vida<=0):vida=0
    if(fome<=0):fome=0
    if(stamina<=0):stamina=0
    if(sono<=0):sono=0
    if(vontade<=0):vontade=0

    statusText = [f"vida: {vida}", f"Fome: {fome}",f"Stamina: {stamina}",f"Sono: {sono}",f"vontade: {vontade}"]

    pygame.draw.rect(window, corSquare, (posAcx, posAcy, QUADRADO_SIZE, QUADRADO_SIZE))
    textoFixolas(20,statusText,0,WHITE,posAcx-11,posAcy-32,QUADRADO_SIZE,QUADRADO_SIZE)
    textoFixolas(20,statusText,1,WHITE,posAcx-7,posAcy-15,QUADRADO_SIZE,QUADRADO_SIZE)
    textoFixolas(20,statusText,2,WHITE,posAcx,posAcy+2,QUADRADO_SIZE,QUADRADO_SIZE)
    textoFixolas(20,statusText,3,WHITE,posAcx-12,posAcy+19,QUADRADO_SIZE,QUADRADO_SIZE)
    textoFixolas(20,statusText,4,WHITE,posAcx-1,posAcy+36,QUADRADO_SIZE,QUADRADO_SIZE)
# Função para mover o personagem
ruaHorizontal = False

tempo_inicial1= datetime.datetime.now()
tempo_inicial2= datetime.datetime.now()
tempo_inicial3= datetime.datetime.now()

#def random_Objetos():

def moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq, limiteFaixaDir, limiteAbaixo):
    global tempo_inicial1,tempo_inicial2,tempo_inicial3,sono,fome,vontade,stamina,VELOCIDADE

    actualStatus()
    tempo_atualFome = datetime.datetime.now()
    tempo_atualVontade = datetime.datetime.now()
    tempo_atualSono = datetime.datetime.now()

    # Calcular a diferença de tempo em segundos
    diferenca_tempo1 = ( tempo_atualFome- tempo_inicial1).total_seconds()
    diferenca_tempo2 = (tempo_atualVontade - tempo_inicial2).total_seconds()
    diferenca_tempo3 = (tempo_atualSono - tempo_inicial3).total_seconds()

    if diferenca_tempo1 >= 13:
        fome -= 1
        stamina -= 1
        # Atualiza o tempo inicial para o próximo ciclo de 10 segundos
        tempo_inicial1 = tempo_atualFome

    if diferenca_tempo2 >= 10:
        vontade -= 1
        # Atualiza o tempo inicial para o próximo ciclo de 15 segundos
        tempo_inicial2 = tempo_atualVontade

    if diferenca_tempo3 >= 35:
        sono -= 1
        # Atualiza o tempo inicial para o próximo ciclo de 20 segundos
        tempo_inicial3 = tempo_atualSono   

    if teclas_pressionadas[pygame.K_w]:
        move_y -= VELOCIDADE
    if teclas_pressionadas[pygame.K_s]:
        move_y += VELOCIDADE
    if teclas_pressionadas[pygame.K_a]:
        move_x -= VELOCIDADE
    if teclas_pressionadas[pygame.K_d]:
        move_x += VELOCIDADE

    next_x = square_x + move_x
    next_y = square_y + move_y
      
    if ruaHorizontal:
        if  not((next_x < limiteFaixaEsq-510 or next_x > limiteFaixaDir+400+QUADRADO_SIZE) or (next_y > limiteAbaixo-430 or next_y < 300 )):
            square_x = next_x
            square_y = next_y

    elif not ruaHorizontal:
        if not ((next_x < limiteFaixaEsq or next_x > limiteFaixaDir) or (next_y > limiteAbaixo)):
            square_x = next_x
            square_y = next_y

    return square_x, square_y


def valorLinha(nome_arquivo, num_linha):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        if num_linha >= 1 and num_linha <= len(linhas):
            linha_especifica = linhas[num_linha - 1].strip()
            return linha_especifica
        else:
            return None

# Função dentro da casa
def casaDentro(moveX, moveY,ruaAtual):
    global enter_pressionado, square_x, square_y,ruaHorizontal,VELOCIDADE,vida,sono,fome,stamina,vontade,teclas_pressionadas  # Declara a variável como global

    ruaHorizontal = False
    posX = JANELA_WIDTH // 2 - SAIDA_WIDTH // 2
    posY = JANELA_HEIGHT - 130
    square_x = posX + (SAIDA_WIDTH // 4)
    square_y = posY
    VELOCIDADE=45


    # Lista de caminhos relativos das imagens

    imagens1= ["images/cama.png","images/cama1.png","images/cama2.png","images/cama3.png","images/cama4.png","images/cama5.png","images/cama6.png"]
    imagem_atual = random.choice(imagens1)
    cama = pygame.image.load(imagem_atual)
    cama = pygame.transform.scale(cama, (700, 900))

    imagens2= ["images/cozinha1.png","images/cozinha2.png","images/cozinha3.png","images/cozinha4.png","images/cozinha5.png"]
    imagem_atual2 = random.choice(imagens2)
    cozinha = pygame.image.load(imagem_atual2)
    cozinha = pygame.transform.scale(cozinha, (700, 900))

    imagens3= ["images/wc1.png","images/wc2.png"]
    imagem_atual3 = random.choice(imagens3)
    wc = pygame.image.load(imagem_atual3)
    wc = pygame.transform.scale(wc, (100, 300))
   
    while True:
        pygame.display.update()
       # Crie objetos Rect para representar o quadrado e a cama
        quadrado_rect = pygame.Rect(square_x, square_y, QUADRADO_SIZE, QUADRADO_SIZE)
        saida_rect = pygame.Rect(posX,posY, SAIDA_WIDTH, SAIDA_HEIGHT)  
        cama_rect = pygame.Rect(1450, -80, 1289, 725)  
        cozinha_rect = pygame.Rect(0, 0, 550,275)  
        wc_rect = pygame.Rect(0, 700, 345, 545)
  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()       

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
               subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) #abrir exit.exe de C
               time.sleep(6)
               pygame.quit()
               sys.exit() 

        if quadrado_rect.colliderect(saida_rect) and teclas_pressionadas[pygame.K_f]:
            VELOCIDADE=20
            ruaAtual()

        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True    

            # Verifique se os objetos Rect colidem
            if quadrado_rect.colliderect(cama_rect) and sono <10:
                # O quadrado colidiu com a cama
                #chamaar o executavel de horas para dormir e feseguir o codigo so dps de fechar o .exe
                subprocess.Popen(["start", "../statusPersonagem/horaDormir/bin//Debug/horaDormir.exe"], shell=True)
                
                verificarcaminho = "../statusPersonagem/verificarFecharEXE.txt"
                while(True):
                    if os.path.exists(verificarcaminho):
                        nValorLinha = int(valorLinha(verificarcaminho,1))
                        if nValorLinha == 6969: break

                caminho = "../statusPersonagem/horasSono.txt"
                valorLinha(caminho,3)
                nValorLinha = int(valorLinha(caminho,3))
                print("Horas a dormir: ",nValorLinha)
                #Apagar o ficheiro .txt para n ter problemas muito mas muito maus...
                
                os.remove(verificarcaminho)

                if nValorLinha > 71:
                    vida = 0 
                    stamina=0
                    vontade=0
                    sono=0
                if nValorLinha > 23:
                    vida -= 2 
                    stamina-=5
                    vontade-=0
                    sono=0
                if nValorLinha > 47:
                    vida -= 5 
                    stamina=0
                    vontade=0
                    sono=0
                if nValorLinha > 7 or nValorLinha > 9: 
                    sono += 10 
                    stamina += 10 
                    fome -= (nValorLinha//10)
                if nValorLinha > 2 and nValorLinha < 8: sono += 3
                if nValorLinha >= 0 and nValorLinha < 3: sono += 1

                if sono >= 10: sono=10
                print("Sono: ",sono)
  
            if quadrado_rect.colliderect(cozinha_rect) and fome <10:
                    subprocess.Popen(["start", "../statusPersonagem/comer/bin/Debug/comer.exe"], shell=True) ##abrir comida.exe de C
                    
                    verificarcaminho = "../statusPersonagem/verificarFecharEXE.txt"
                    while(True):
                        if os.path.exists(verificarcaminho):
                            nValorLinha = int(valorLinha(verificarcaminho,1))
                            if nValorLinha == 6969: break

                    caminho = "../statusPersonagem/comida.txt"
                    valorLinha(caminho,3)
                    nValorLinha = int(valorLinha(caminho,3))
                    print("A comida: ",nValorLinha)
                    
                    #Apagar o ficheiro .txt para n ter problemas muito mas muito maus...
                    os.remove(verificarcaminho)

                    if nValorLinha == 1: fome += 3
                    if nValorLinha == 2: fome += 2 
                    if nValorLinha == 14: fome += 4
                    if nValorLinha == 15: fome += 4

                    if fome >= 10: fome=10
                    print("fome: ",fome)
              
            if quadrado_rect.colliderect(wc_rect) and vontade <10:
                    subprocess.Popen(["start", "../statusPersonagem/vontade/bin/Debug/vontade.exe"], shell=True) ##abrir comida.exe de C
                    
                    verificarcaminho = "../statusPersonagem/verificarFecharEXE.txt"
                    while(True):
                        if os.path.exists(verificarcaminho):
                            nValorLinha = int(valorLinha(verificarcaminho,1))
                            if nValorLinha == 6969: break

                    caminho = "../statusPersonagem/vontade.txt"
                    valorLinha(caminho,3)
                    nValorLinha = int(valorLinha(caminho,3))
                    print("A vontade: ",nValorLinha)
                    
                    #Apagar o ficheiro .txt para n ter problemas muito mas muito maus...
                    os.remove(verificarcaminho)

                    if nValorLinha == 5: vontade += 5
                    if nValorLinha == 10: vontade += 10 

                    if vontade >= 10: vontade=10
                    
                    print("Vontade: ",vontade)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        pygame.display.update()
        limiteJanelaDir = JANELA_WIDTH - QUADRADO_SIZE
        square_x, square_y = moverPersonagem(square_x, square_y, moveX, moveY, teclas_pressionadas, 0, limiteJanelaDir,JANELA_HEIGHT - 120)
         
        print("Quadrado movido para ({}, {})".format(square_x, square_y))

         #limites do jogo
        if square_y <= 10:
           square_y = 10

        # Limpa a tela
        window.fill(BLACK)

        desenharFundo(BROWN_DARK)
        desenharSaida(BROWN_LIGHT, posX, posY)

        textoFixolas(40,saidaCasa,0,WHITE, posX, posY,SAIDA_WIDTH,SAIDA_HEIGHT)

        cama = pygame.image.load(imagem_atual)
        window.blit(cama, (1300, -80)) #Mostrar camas

        cozinha = pygame.image.load(imagem_atual2)
        window.blit(cozinha, (0, 0)) #Mostrar cozinha

        wc = pygame.image.load(imagem_atual3)
        window.blit(wc, (0, 600)) #Mostrar cozinha

        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)


        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def rFixe():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verificarVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE, ruaHorizontal,startHorizontalX,startHorizontalY
    global VELOCIDADE
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = True
 
    square_x = startHorizontalX
    square_y = startHorizontalY
    
    if verificarVoltar:
        square_x = posAtualX
        square_y = posAtualY
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True

            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i
                
                if (1400 <= square_x <= 1580 and square_y == 670) or (960 <= square_x <= 1140 and square_y == 670) or (540 <= square_x <= 700 and square_y == 670) or (100 <= square_x <= 280 and square_y == 670):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rFixe)

            for i, nome in enumerate(nomes_casas_direita):
                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (1400 <= square_x <= 1580 and square_y == 310) or (960 <= square_x <= 1140 and square_y == 310) or (540 <= square_x <= 700 and square_y == 310) or (100 <= square_x <= 280 and square_y == 310):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rFixe)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)

        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        # Verifique se as coordenadas do personagem estão dentro do intervalo
        if 310 <= square_y <= 670 and square_x == 1900: ##direita
           verificarVoltar = True
           posAtualX = 0
           posAtualY = 490
           rTeuPai()
        if 310 <= square_y <= 670 and square_x == -60: #Esquerda
           verificarVoltar2 = True
           posAbaixox = 1330
           posAbaixoy =  890
           rFinish()
           
        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4
        CASAS_SIZE = width // 10

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,5,WHITE,JANELA_WIDTH//5 , JANELA_HEIGHT//2,FAIXAS_WIDTH+800,JANELA_HEIGHT//16)
        #Desenhar faixas com um rua
        desenharFaixas(YELLOW,JANELA_WIDTH-1920,0,JANELA_WIDTH,JANELA_HEIGHT//3,JANELA_WIDTH-1920,JANELA_HEIGHT-330,JANELA_WIDTH,JANELA_HEIGHT//3)
        #ddesenhar bordes faixas
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT//3,JANELA_WIDTH, 10))
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT-340,JANELA_WIDTH, 10))
        # Desenhar casas do lado esquerdo
        
        # Desenhar casas do lado esquerdo
        casa_y = (JANELA_HEIGHT - 820) - CASAS_SIZE  # Posição Y fixa para todas as casas
        casa_spacing = CASAS_SIZE + 50  # Espaçamento entre as casas

        for i, nome in enumerate(nomes_casas_esquerda):
            casa_x = 2+JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, RED, PINK,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)

        # Desenhar casas do lado direito
        casa_y = (JANELA_HEIGHT - 50) - CASAS_SIZE  # Posição Y fixa para todas as casas

        for i, nome in enumerate(nomes_casas_direita):
            casa_x = JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y,  RED, PINK,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)


        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def rTeuPai():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verific,arVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE, ruaHorizontal,startHorizontalX,startHorizontalY,verificarVoltar
     
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = True
    
    square_x = startHorizontalX
    square_y = startHorizontalY
    
    if verificarVoltar:
      square_x = posAtualX
      square_y = posAtualY

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True

            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (1400 <= square_x <= 1580 and square_y == 670) or (960 <= square_x <= 1140 and square_y == 670) or (540 <= square_x <= 700 and square_y == 670) or (100 <= square_x <= 280 and square_y == 670):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rTeuPai)

            for i, nome in enumerate(nomes_casas_direita):
                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (1400 <= square_x <= 1580 and square_y == 310) or (960 <= square_x <= 1140 and square_y == 310) or (540 <= square_x <= 700 and square_y == 310) or (100 <= square_x <= 280 and square_y == 310):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rTeuPai)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)

        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        # Verifique se as coordenadas do personagem estão dentro do intervalo
        if 310 <= square_y <= 670 and square_x == 1900:
           verificarVoltar2 = True
           posAbaixox = 430
           posAbaixoy =  890
           rFinish()
        if 310 <= square_y <= 670 and square_x == -80:
           verificarVoltar = True
           posAtualX = 1800
           posAtualY = 490
           rFixe()
           

        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4
        CASAS_SIZE = width // 10

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,4,WHITE,JANELA_WIDTH//5 , JANELA_HEIGHT//2,FAIXAS_WIDTH+800,JANELA_HEIGHT//16)
        #Desenhar faixas com um rua
        desenharFaixas(BLUE,JANELA_WIDTH-1920,0,JANELA_WIDTH,JANELA_HEIGHT//3,JANELA_WIDTH-1920,JANELA_HEIGHT-330,JANELA_WIDTH,JANELA_HEIGHT//3)
        #ddesenhar bordes faixas
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT//3,JANELA_WIDTH, 10))
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT-340,JANELA_WIDTH, 10))
        # Desenhar casas do lado esquerdo
        
        # Desenhar casas do lado esquerdo
        casa_y = (JANELA_HEIGHT - 820) - CASAS_SIZE  # Posição Y fixa para todas as casas
        casa_spacing = CASAS_SIZE + 50  # Espaçamento entre as casas

        for i, nome in enumerate(nomes_casas_esquerda):
            casa_x = 2+JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, BLACK, GRAY,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)

        # Desenhar casas do lado direito
        casa_y = (JANELA_HEIGHT - 50) - CASAS_SIZE  # Posição Y fixa para todas as casas

        for i, nome in enumerate(nomes_casas_direita):
            casa_x = JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, BLACK, GRAY,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)


        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def rFinish():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verificarVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE,ruaHorizontal
     
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = False
    
    square_x = posAtualX
    square_y = posAtualY

    if verificarVoltar2:
      square_x = posAbaixox
      square_y = posAbaixoy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True
            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar2 = False
                    posAtualX = square_x
                    posAtualY = square_y
                    casaDentro(move_x, move_y,rFinish)

            for i, nome in enumerate(nomes_casas_direita):
                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar2 = False
                    posAtualX = square_x
                    posAtualY = square_y
                    casaDentro(move_x, move_y,rFinish)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)
 
        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        if  830 <= square_y <= 1030 and square_x == 430:
            # Movimentação permitida
            verificarVoltar =True
            posAtualX = 1780
            posAtualY = 490
            rTeuPai()
        if  830 <= square_y <= 1030 and square_x == 1370:
            verificarVoltar =True
            posAtualX = -20
            posAtualY = 490
            rFixe()

        if square_y == -110: #se sobes demais, voltas ao inicio
           #Verificar se saiu da janela da parte de abaixo e posicionar o personagem na parte de cima da outra tela de jogo
           verificarVoltar = True
           posAcimax = 900
           posAcimay =  950
           CASAS_SIZE = width // 10
           main()

        if square_y == limiteAbaixo:
           #Verificar se saiu da janela da parte de abaixo e posicionar o personagem na parte de cima da outra tela de jogo
           verificarVoltar2 = True
           posAbaixox = (JANELA_WIDTH // 2)-50
           posAbaixoy =  JANELA_HEIGHT//300
           rDoLadrao()
           


        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,6,WHITE, JANELA_WIDTH // 2 - (QUADRADO_SIZE+95), JANELA_HEIGHT//3,FAIXAS_WIDTH,FAIXAS_WIDTH-200)
        textoFixolas(60,nomesRuas,5,WHITE,JANELA_WIDTH//2.5 , JANELA_HEIGHT//2.6,JANELA_WIDTH,JANELA_HEIGHT)
        textoFixolas(60,nomesRuas,4,WHITE,JANELA_WIDTH-2700 , JANELA_HEIGHT//2.6,JANELA_WIDTH,JANELA_HEIGHT)
        #Desenhar faixas com tres ruas
        desenharFaixas(ORANGE,0,0,FAIXAS_WIDTH,JANELA_HEIGHT-250,JANELA_WIDTH-FAIXAS_WIDTH,0,FAIXAS_WIDTH,JANELA_HEIGHT-250)

        # Desenhar casas do lado esquerdo
        for i, nome in enumerate(nomes_casas_esquerda):
            house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
            house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y, PURPLE, PURPLE_LIGTH,300,100)
            textoFixolasCasas(fontCasa,WHITE, house_x, house_y, nome)
        # Desenhar casas do lado direito
        for i, nome in enumerate(nomes_casas_direita):
            house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
            house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y,PURPLE, PURPLE_LIGTH,300,100)
            textoFixolasCasas(fontCasa,WHITE, house_x, house_y, nome)
        # Desenha o quadrado

        #pygame.draw.rect(window, WHITE, (430, FAIXAS_WIDTH+350, 10, QUADRADO_SIZE*2))

        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def rStreet():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verificarVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE, ruaHorizontal,startHorizontalX,startHorizontalY
     
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = True
 
    square_x = startHorizontalX
    square_y = startHorizontalY
    
    if verificarVoltar:
        square_x = posAtualX
        square_y = posAtualY

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True

            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):

                if (1400 <= square_x <= 1580 and square_y == 670) or (960 <= square_x <= 1140 and square_y == 670) or (540 <= square_x <= 700 and square_y == 670) or (100 <= square_x <= 280 and square_y == 670):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rStreet)

            for i, nome in enumerate(nomes_casas_direita):

                if (1400 <= square_x <= 1580 and square_y == 310) or (960 <= square_x <= 1140 and square_y == 310) or (540 <= square_x <= 700 and square_y == 310) or (100 <= square_x <= 280 and square_y == 310):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rStreet)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)

        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        # Verifique se as coordenadas do personagem estão dentro do intervalo
        if 310 <= square_y <= 670 and square_x == 1900: ##direita
           verificarVoltar = True
           posAtualX = 0
           posAtualY = 490
           rATM()
        if 310 <= square_y <= 670 and square_x == -60: #Esquerda
           verificarVoltar2 = True
           posAbaixox = 1330
           posAbaixoy =  890
           rDoLadrao()
           

        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4
        CASAS_SIZE = width // 10

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,2,WHITE,JANELA_WIDTH//5 , JANELA_HEIGHT//2,FAIXAS_WIDTH+800,JANELA_HEIGHT//16)
        #Desenhar faixas com um rua
        desenharFaixas(YELLOW,JANELA_WIDTH-1920,0,JANELA_WIDTH,JANELA_HEIGHT//3,JANELA_WIDTH-1920,JANELA_HEIGHT-330,JANELA_WIDTH,JANELA_HEIGHT//3)
        #ddesenhar bordes faixas
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT//3,JANELA_WIDTH, 10))
        pygame.draw.rect(window, BLACK, (JANELA_WIDTH-1920, JANELA_HEIGHT-340,JANELA_WIDTH, 10))
        # Desenhar casas do lado esquerdo
        
        # Desenhar casas do lado esquerdo
        casa_y = (JANELA_HEIGHT - 820) - CASAS_SIZE  # Posição Y fixa para todas as casas
        casa_spacing = CASAS_SIZE + 50  # Espaçamento entre as casas

        for i, nome in enumerate(nomes_casas_esquerda):
            casa_x = 2+JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, ORANGE, BROWN_DARK,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)

        # Desenhar casas do lado direito
        casa_y = (JANELA_HEIGHT - 50) - CASAS_SIZE  # Posição Y fixa para todas as casas

        for i, nome in enumerate(nomes_casas_direita):
            casa_x = JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, ORANGE, BROWN_DARK,100,300)
            textoFixolasCasas(fontCasa, WHITE, casa_x, casa_y, nome)


        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

startHorizontalX = (JANELA_WIDTH //2)+780
startHorizontalY= JANELA_HEIGHT //2.2

def rATM():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verific,arVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE, ruaHorizontal,startHorizontalX,startHorizontalY,verificarVoltar
     
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = True
    
    square_x = startHorizontalX
    square_y = startHorizontalY
    
    if verificarVoltar:
      square_x = posAtualX
      square_y = posAtualY

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True

            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (1400 <= square_x <= 1580 and square_y == 670) or (960 <= square_x <= 1140 and square_y == 670) or (540 <= square_x <= 700 and square_y == 670) or (100 <= square_x <= 280 and square_y == 670):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rATM)

            for i, nome in enumerate(nomes_casas_direita):
                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (1400 <= square_x <= 1580 and square_y == 310) or (960 <= square_x <= 1140 and square_y == 310) or (540 <= square_x <= 700 and square_y == 310) or (100 <= square_x <= 280 and square_y == 310):
                    verificarVoltar = False
                    startHorizontalX = square_x
                    startHorizontalY = square_y
                    casaDentro(move_x, move_y,rATM)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)

        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        #limiteFaixaEsq-510           next_x > limiteFaixaDir+370
        # Verifique se as coordenadas do personagem estão dentro do intervalo
        if 310 <= square_y <= 670 and square_x == 1900:
           verificarVoltar2 = True
           posAbaixox = 430
           posAbaixoy =  890
           rDoLadrao()
        if 310 <= square_y <= 670 and square_x == -80:
           verificarVoltar = True
           posAtualX = 1800
           posAtualY = 490
           rStreet()


        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4
        CASAS_SIZE = width // 10

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,1,WHITE,JANELA_WIDTH//5 , JANELA_HEIGHT//2,FAIXAS_WIDTH+800,JANELA_HEIGHT//16)
        #Desenhar faixas com um rua
        desenharFaixas(PINK,JANELA_WIDTH-1920,0,JANELA_WIDTH,JANELA_HEIGHT//3,JANELA_WIDTH-1920,JANELA_HEIGHT-330,JANELA_WIDTH,JANELA_HEIGHT//3)
        #ddesenhar bordes faixas
        pygame.draw.rect(window, WHITE, (JANELA_WIDTH-1920, JANELA_HEIGHT//3,JANELA_WIDTH, 10))
        pygame.draw.rect(window, WHITE, (JANELA_WIDTH-1920, JANELA_HEIGHT-340,JANELA_WIDTH, 10))
        # Desenhar casas do lado esquerdo
        
        # Desenhar casas do lado esquerdo
        casa_y = (JANELA_HEIGHT - 820) - CASAS_SIZE  # Posição Y fixa para todas as casas
        casa_spacing = CASAS_SIZE + 50  # Espaçamento entre as casas

        for i, nome in enumerate(nomes_casas_esquerda):
            casa_x = 2+JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, GREEN, GREEN_DARK,100,300)
            textoFixolasCasas(fontCasa, BLACK, casa_x, casa_y, nome)

        # Desenhar casas do lado direito
        casa_y = (JANELA_HEIGHT - 50) - CASAS_SIZE  # Posição Y fixa para todas as casas

        for i, nome in enumerate(nomes_casas_direita):
            casa_x = JANELA_WIDTH - (CASAS_SIZE + casa_spacing) * (i + 1)

            desenharCasa(casa_x, casa_y, GREEN, GREEN_DARK,100,300)
            textoFixolasCasas(fontCasa, BLACK, casa_x, casa_y, nome)


        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def rDoLadrao():
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verificarVoltar,verificarVoltar2,posAbaixox,posAbaixoy,CASAS_SIZE,ruaHorizontal
     
    fontCasa = pygame.font.Font(None, 40)
    surface = pygame.display.get_surface()
    width, height = surface.get_width(), surface.get_height()   
    CASAS_SIZE = width // 14
    ruaHorizontal = False
    
    square_x = posAtualX
    square_y = posAtualY

    if verificarVoltar2:
      square_x = posAbaixox
      square_y = posAbaixoy
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True
            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar2 = False
                    posAtualX = square_x
                    posAtualY = square_y
                    casaDentro(move_x, move_y,rDoLadrao)

            for i, nome in enumerate(nomes_casas_direita):
                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
                house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i

                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar2 = False
                    posAtualX = square_x
                    posAtualY = square_y
                    casaDentro(move_x, move_y,rDoLadrao)

        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT+30
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)
 
        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        if square_y < -110:
           #Verificar se saiu da janela da parte de abaixo e posicionar o personagem na parte de cima da outra tela de jogo
           verificarVoltar2 = True
           posAbaixox =(JANELA_WIDTH // 2)-50
           posAbaixoy =  JANELA_HEIGHT-70
           rFinish()

        if  830 <= square_y <= 1030 and square_x == 430:
            # Movimentação permitida
            verificarVoltar =True
            posAtualX = 1780
            posAtualY = 490
            rATM()
        if  830 <= square_y <= 1030 and square_x == 1370:
            verificarVoltar =True
            posAtualX = -20
            posAtualY = 490
            rStreet()

        if square_y >= 1050:
           #Verificar se saiu da janela da parte de abaixo e posicionar o personagem na parte de cima da outra tela de jogo
           verificarVoltar = True
           posAcimax = 910
           posAcimay = -17
           #isto e para as casa estiverem do mesmo tamanho
           CASAS_SIZE = width // 10
           main()

        # Obtém a superfície da janela atual
        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,3,WHITE, JANELA_WIDTH // 2 - (QUADRADO_SIZE+95), JANELA_HEIGHT//3,FAIXAS_WIDTH,FAIXAS_WIDTH-200)
        textoFixolas(60,nomesRuas,2,WHITE,JANELA_WIDTH//2.5 , JANELA_HEIGHT//2.6,JANELA_WIDTH,JANELA_HEIGHT)
        textoFixolas(60,nomesRuas,1,WHITE,JANELA_WIDTH-2700 , JANELA_HEIGHT//2.6,JANELA_WIDTH,JANELA_HEIGHT)
        #Desenhar faixas com tres ruas
        desenharFaixas(BROWN_LIGHT,0,0,FAIXAS_WIDTH,JANELA_HEIGHT-250,JANELA_WIDTH-FAIXAS_WIDTH,0,FAIXAS_WIDTH,JANELA_HEIGHT-250)

        # Desenhar casas do lado esquerdo
        for i, nome in enumerate(nomes_casas_esquerda):
            house_x = FAIXAS_WIDTH - CASAS_SIZE * 2.3
            house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y, GREEN, GREEN_DARK,300,100)
            textoFixolasCasas(fontCasa,BLACK, house_x, house_y, nome)
        # Desenhar casas do lado direito
        for i, nome in enumerate(nomes_casas_direita):
            house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.6
            house_y = (JANELA_HEIGHT - 450) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y, GREEN, GREEN_DARK,300,100)
            textoFixolasCasas(fontCasa,BLACK, house_x, house_y, nome)
        # Desenha o quadrado

        #pygame.draw.rect(window, WHITE, (430, FAIXAS_WIDTH+350, 10, QUADRADO_SIZE*2))

        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(40)

def main() :
    global enter_pressionado,FAIXAS_WIDTH,QUADRADO_SIZE,square_x,square_y,posAtualX,posAtualY,posAcimax,posAcimay,verificarVoltar,verificarVoltar2,posAbaixox,posAbaixoy,ruaHorizontal
    
    fontCasa = pygame.font.Font(None, 40)
    # Obtém a superfície da janela atual
    ruaHorizontal = False

    square_x = posAtualX
    square_y = posAtualY

    if verificarVoltar:
      square_x = posAcimax
      square_y = posAcimay

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_x = 0
        move_y = 0

        # Obtém o estado de todas as teclas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_ESCAPE]:
            subprocess.Popen(["start", "../statusPersonagem/exit.exe"], shell=True) ##abrir exit.exe de C
            time.sleep(6)
            pygame.quit()
            sys.exit()
        if teclas_pressionadas[pygame.K_RETURN] and not enter_pressionado:
            enter_pressionado = True

            # Verifica se o quadrado está próximo o suficiente de uma casa selecionada
            for i, nome in enumerate(nomes_casas_esquerda):
                house_x = FAIXAS_WIDTH - CASAS_SIZE * 1.7
                house_y = (JANELA_HEIGHT - 250) - (CASAS_SIZE + 60) * i
                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar = False
                    posAtualX = square_x
                    posAtualY = square_y
                    #if not square_y >= -25 and square_y <= 125 and square_x == 1350:
                    casaDentro(move_x, move_y,main)
                    #else:
                     #   print("Escola")

                house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.4
                house_y = (JANELA_HEIGHT - 250) - (CASAS_SIZE + 60) * i

                if (abs(house_x - square_x) < 300 and abs(house_y - square_y) < 100):
                    verificarVoltar = False
                    posAtualX = square_x
                    posAtualY = square_y
                    casaDentro(move_x, move_y,main)


        elif not teclas_pressionadas[pygame.K_RETURN]:
            enter_pressionado = False

        limiteFaixaEsq = FAIXAS_WIDTH - 60
        limiteFaixaDir = JANELA_WIDTH - QUADRADO_SIZE // 2 - FAIXAS_WIDTH
        limiteAbaixo = JANELA_HEIGHT - 120
        # Chama a função moverPersonagem() para atualizar as coordenadas do quadrado
        square_x, square_y = moverPersonagem(square_x, square_y, move_x, move_y, teclas_pressionadas, limiteFaixaEsq,limiteFaixaDir, limiteAbaixo)

        #print("Quadrado movido para ({}, {})".format(square_x, square_y))

        acima = JANELA_HEIGHT-1180
        #Verificar se o cuadrado esta afora da janel da parte de cima, se esta, vai para a proxima Rua
        if square_y < acima:
           #Verificar se saiu da janela da parte de abaixo e posicionar o personagem na parte de cima da outra tela de jogo
           verificarVoltar2 = True
           posAbaixox =(JANELA_WIDTH // 2)-50
           posAbaixoy =  JANELA_HEIGHT-70
           rDoLadrao()

        surface = pygame.display.get_surface()
        width, height = surface.get_width(), surface.get_height()    

        # Atraso de 10 milissegundos

        # Atualiza as dimensões e posições com base no tamanho da janela
        QUADRADO_SIZE = height // 8
        FAIXAS_WIDTH = width // 4

        # Limpa a tela
        window.fill(BLACK)
        # Desenhando a rua
        desenharFundo(GRAY)
        #Nome Rua
        textoFixolas(100,nomesRuas,0,WHITE, JANELA_WIDTH // 2 - (QUADRADO_SIZE+95), JANELA_HEIGHT//3,FAIXAS_WIDTH,FAIXAS_WIDTH)
        #Desenhar faixas com uma ruas
        desenharFaixas(GREEN_DARK,0,0,FAIXAS_WIDTH,JANELA_HEIGHT,JANELA_WIDTH-FAIXAS_WIDTH,0,FAIXAS_WIDTH,JANELA_HEIGHT)
        
        

        # Desenhar casas do lado esquerdo
        for i, nome in enumerate(nomes_casas_esquerda):
            house_x = FAIXAS_WIDTH - CASAS_SIZE * 1.7
            house_y = (JANELA_HEIGHT - 250) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y, BROWN_LIGHT, BROWN_DARK,300,100)
            textoFixolasCasas(fontCasa,BLACK, house_x, house_y, nome)
        # Desenhar casas do lado direito
        for i, nome in enumerate(nomes_casas_direita):
            house_x = JANELA_WIDTH - FAIXAS_WIDTH / 1.4
            house_y = (JANELA_HEIGHT - 250) - (CASAS_SIZE + 60) * i
            desenharCasa(house_x, house_y, BROWN_LIGHT, BROWN_DARK,300,100)
            textoFixolasCasas(fontCasa,BLACK, house_x, house_y, nome)
        # Desenha o quadrado
        desenharQuadrado(BLACK, square_x, square_y)

        # Atualiza a janela
        pygame.display.update()
        clock.tick(60)

def morrer():
    print("To bue morto")
    subprocess.Popen(["start", "../statusPersonagem/again.exe"], shell=True) ##abrir exit.exe de C
    time.sleep(6)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()