import pygame
from pygame.locals import *
from sys import exit
from random import randint
# Aula 1 - Pygame

# Inicializa o Pygame
pygame.init()

pygame.mixer.music.set_volume(0.3)
musicaFundo = pygame.mixer.music.load("Jogo 1/Sons/Trilha Sonora.mp3")
pygame.mixer.music.play(-1)

somganhou = pygame.mixer.Sound("Jogo 1/Sons/ganhou.wav")
sommorreu = pygame.mixer.Sound("Jogo 1/Sons/Morreu.wav")

# Definindo a tela
largura = 640
altura = 480
xret = int(largura / 2)
yret = 0
xcircle = 0
ycircle = int(altura / 2 )
fonte = pygame.font.SysFont("arial", 30, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aula 1 - Pygame")
relogio = pygame.time.Clock()

# Loop do jogo principal
while True:
    relogio.tick(1000)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {pontos}" 
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            print(f"Pontos: {pontos}" )
            pygame.quit()
            exit()
            

# Movimentação do círculo
        '''
        if event.type == KEYDOWN:
            if event.key == K_w:
                ycircle -= 30
            elif event.key == K_s:
                ycircle += 30
            elif event.key == K_a:
                xcircle -= 30
            elif event.key == K_d:
                xcircle += 30'''
        
        if pygame.key.get_pressed()[K_w]:
            ycircle -= 10
        if pygame.key.get_pressed()[K_s]:       
            ycircle += 10                      
        if pygame.key.get_pressed()[K_a]:
            xcircle -= 10
        if pygame.key.get_pressed()[K_d]:
            xcircle += 10

# Colisão do círculo com as bordas da tela
    if xcircle < 0:
        xcircle = 0
    if xcircle > largura:
        xcircle = largura
    if ycircle < 0:
        ycircle = 0
    if ycircle > altura:
        ycircle = altura

# Desenha um retângulo na tela
    ret = pygame.draw.rect(tela, (255, 50, 255), (xret, yret, 60, 50))
    yret += 1
    if  yret > altura:
        yret = 0

# Desenha um círculo na tela
    circulo = pygame.draw.circle(tela, (0, 250, 250), (xcircle, ycircle), 20)


# Colisão do retângulo com o círculo
    if ret.colliderect(circulo):
        print("Morreu")
        sommorreu.play()
        xcircle = 0
        ycircle = altura / 2

# Desenha um  de chegada na tela
    linha = pygame.draw.line(tela, (0, 255, 0), (600, 0), (600, altura), 20)
    if linha.colliderect(circulo):
        print("Ganhou")
        somganhou.play()
        xcircle = 0
        ycircle = altura / 2
        pontos += 1

# Desenha os pontos na tela
    tela.blit(texto_formatado, (10, 10))
# Atualiza a tela
    pygame.display.update()
