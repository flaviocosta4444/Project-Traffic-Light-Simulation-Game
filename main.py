import pygame
from interface import Menu

# Iniciar o programa
pygame.init()

# Dimensão da janela
screen = pygame.display.set_mode((0, 0), pygame. FULLSCREEN|pygame.NOFRAME)

# Dimensionar a janela
screen_width, screen_height = pygame.display.get_surface().get_size()

# Chama o menu
Menu.menu_inicial(screen,screen_width,screen_height)