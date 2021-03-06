# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

from config import WIDTH, HEIGHT
from game_screen import game_screen

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Navinha")

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
