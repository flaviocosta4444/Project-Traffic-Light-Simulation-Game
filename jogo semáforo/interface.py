import pygame
from regras import Regras
from modo_jogo import Modo_Jogo

pygame.init()

class Menu:
    def menu_inicial(screen,screen_width,screen_height):
        # Carrega o background
        background_image = pygame.image.load(r"C:\Users\FLÁVIOMIGUELGOMESCOS\Desktop\imagens_semáforo\imagem_menu.png").convert()  
        # Redimensionar imagem
        background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))
        
        # Defenifir cores
        branco = (255, 255, 255)
        laranja = (255, 70, 0)
        preto = (0, 0, 0)
        cinza = (128, 128, 128)
        ciano = (0, 255, 255)
        vermelho = (205, 50, 50)
        verde = (0, 128, 0)
        amarelo = (255, 255, 50)

        # Definir fonte
        font_menu = pygame.font.SysFont(None, 40)

        # Definir os textos dos botões
        button_play_text = font_menu.render("Iniciar Jogo", True, preto)
        button_load_text = font_menu.render("Carregar Partida", True, preto)
        button_rules_text = font_menu.render("Regras", True, preto)
        button_leave_text = font_menu.render("Sair", True, preto)


        # Definir as posições dos botões
        button_play_pos = button_play_text.get_rect(center=(screen_width/2, 245))
        button_load_pos = button_load_text.get_rect(center=(screen_width/2, 345))
        button_rules_pos = button_rules_text.get_rect(center=(screen_width/2, 445))
        button_leave_pos = button_leave_text.get_rect(center=(screen_width/2, 545))

        # Loop principal do jogo
        running = True
        while running:

        # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar se o clique foi em um dos botões
                    mouse_pos = pygame.mouse.get_pos()
                    if button_play_pos.collidepoint(mouse_pos):
                        Modo_Jogo.Modo(screen,screen_width,screen_height) 
                    elif button_load_pos.collidepoint(mouse_pos):
                        print("lido")
                    elif button_rules_pos.collidepoint(mouse_pos):
                        Regras.mostrar_regras(screen,screen_width,screen_height) 
                    elif button_leave_pos.collidepoint(mouse_pos):
                        pygame.QUIT()
            screen.blit(background_image, (0, 0))  

            # Desenhar os botões na tela
            pygame.draw.rect(screen, vermelho, (640, 200, 250, 80), 50)
            screen.blit(button_play_text, button_play_pos)
            pygame.draw.rect(screen, amarelo, (640, 300, 250, 80), 50)
            screen.blit(button_load_text, button_load_pos)
            pygame.draw.rect(screen, verde, (640, 400, 250, 80), 50)
            screen.blit(button_rules_text, button_rules_pos)
            pygame.draw.rect(screen, cinza, (640, 500, 250, 80), 50)
            screen.blit(button_leave_text, button_leave_pos)
            pygame.display.update()
        

pygame.quit()