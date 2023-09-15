import os
import random
import glob
import pygame
import math

from pygame.locals import *

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((1000, 1000), RESIZABLE)
pygame.display.set_caption('Visualizador de Imagens Aleatórias')

diretorio_imagens = 'CAMINHO PRA PASTA DA IMAGEM AQUI'
tela_redimensionada = False


lista_imagens = [arquivo for arquivo in glob.iglob(os.path.join(diretorio_imagens, '**', '*.jpg'), recursive=True)]

imagem_atual = pygame.image.load(os.path.join(diretorio_imagens, lista_imagens[0]))
imagem_atual = pygame.transform.scale(imagem_atual, (largura, altura))

largura_tela = 1000
altura_tela = 1000
def redimensionar_imagem(nova_largura, nova_altura):
    if imagem_atual.get_height() > nova_altura:
        teste = nova_altura /(imagem_atual.get_height())
        imagemScaled = pygame.transform.scale(imagem_atual, (imagem_atual.get_width()*teste, imagem_atual.get_height()*teste))
    elif imagem_atual.get_width() > nova_largura:
        teste = nova_largura /(imagem_atual.get_width())
        imagemScaled = pygame.transform.scale(imagem_atual, (imagem_atual.get_width()*teste, imagem_atual.get_height()*teste))
    else:
        imagemScaled = pygame.transform.scale(imagem_atual, (nova_largura, nova_altura))
    return imagemScaled



rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
    
            imagem_atual = pygame.image.load(os.path.join(diretorio_imagens, random.choice(lista_imagens)))
            imagem_atual = redimensionar_imagem(largura_tela, altura_tela)
        elif evento.type == pygame.VIDEORESIZE:
            largura_tela, altura_tela = evento.size
            tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
            tela_redimensionada = True
    if tela_redimensionada:
        imagem_atual = redimensionar_imagem(largura_tela, altura_tela)
        tela_redimensionada = False

    tela.fill((0, 0, 0))

    paddingW = math.floor((tela.get_width()- imagem_atual.get_width())/2)
    paddingH = math.floor((tela.get_height()- imagem_atual.get_height())/2)

    tela.blit(imagem_atual, (paddingW,paddingH))

    pygame.display.flip()

# Encerre o Pygame
pygame.quit()


