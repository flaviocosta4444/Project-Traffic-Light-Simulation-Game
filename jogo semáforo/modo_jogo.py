import pygame
from escolher_nome_jogadores import Escolher_Nome
from escolher_nome_bot import Escolher_Nome_Bot
pygame.init()

class Modo_Jogo:
    def Modo(screen,screen_width,screen_height):

        # Carrega o background
        background_image = pygame.image.load(r"C:\Users\FLÁVIOMIGUELGOMESCOS\Desktop\imagens_semáforo\escolher.jpg").convert()  
        # Redimensionar imagem
        background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))

         # Definir fonte
        font = pygame.font.SysFont(None, 40)

         # Definir cores
        branco = (255, 255, 255)
        cinza = (128, 128, 128)
        vermelho = (205, 50, 50)
        preto = (0, 0, 0)
        ciano = (0, 255, 255)

        # Definir os textos dos botões
        button_escolher_text = font.render("Clique Aqui", True, preto)
        button_escolher_text2 = font.render("Clique Aqui", True, preto)
        button_voltar_text = font.render("Voltar", True, preto)

        # Definir as posições dos botões
        button_escolher_pos = button_escolher_text.get_rect(center=(500, 435))
        button_escolher_pos2 = button_escolher_text2.get_rect(center=(1050, 435))
        button_voltar_pos = button_voltar_text.get_rect(center=(770, 470))


        running = True
        while running:
            
        # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar se o clique foi em um dos botões
                    mouse_pos = pygame.mouse.get_pos()
                    if button_escolher_pos.collidepoint(mouse_pos):
                       n1,n2 = Escolher_Nome.escolhaNomes(screen,screen_width,screen_height)
                    if button_escolher_pos2.collidepoint(mouse_pos):
                        Escolher_Nome_Bot.escolhaNomeBot(screen,screen_width,screen_height)
                    if button_voltar_pos.collidepoint(mouse_pos):
                        return 

            
            # Dar blit na tela
            screen.blit(background_image, (0, 0))
            screen.blit(button_escolher_text, button_escolher_pos)
            screen.blit(button_escolher_text2, button_escolher_pos2)
            pygame.draw.rect(screen, vermelho, (670, 420, 200, 85), 50)
            screen.blit(button_voltar_text, button_voltar_pos)

            # Atualiza a tela
            pygame.display.update()