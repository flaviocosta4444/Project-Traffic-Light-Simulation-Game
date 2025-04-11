import pygame
from teste_pvp import Iniciar_Jogo

class Escolher_Nome:
    def escolhaNomes(screen,screen_width,screen_height):

        # Carrega o background
        background_image = pygame.image.load(r"C:\Users\FLÁVIOMIGUELGOMESCOS\Desktop\imagens_semáforo\rrrr.png").convert()  
        # Redimensionar imagem
        background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))
        # Definir fonte
        font2 = pygame.font.Font(None, 40)
        font = pygame.font.Font(None, 30)

        # Definir Cores
        preto = (0, 0, 0)
        vermelho = (205, 50, 50)

        # Definir posição da caixa de texto
        input_rect = pygame.Rect(140, 80, 435, 100)
        area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
        user_text = ''
        nome1 = ''

        input_rect2 = pygame.Rect(140, 220, 435, 100)
        area_sair_escolhaNomes2 = pygame.Rect(13, 665, 100, 100)
        user_text2 = ''
        nome2 = ''

        # Definir os textos dos botões
        button_escrever_text = font.render("Escreva o nome do Jogador 1:", True, preto)
        button_escrever_text2 = font.render("Escreva o nome do Jogador 2:", True, preto)
        button_voltar_text = font2.render("Voltar", True, preto)

        button_escrever_pos = button_escrever_text.get_rect(center=(180, 120))
        button_escrever_pos2 = button_escrever_text.get_rect(center=(180, 180))
        button_voltar_pos = button_voltar_text.get_rect(center=(770, 470))
        dy=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_voltar_pos.collidepoint(mouse_pos):
                        return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if nome1 == '':
                            nome1 = user_text
                            dy=60
                            user_text= ''
                        elif nome2 == '':
                            nome2 = user_text
                            text_surface2 = font.render(user_text, True, preto) 
                            screen.blit(text_surface2, (input_rect2.x + 200, input_rect2.y + 10))
                            input_rect2.w = max(435, text_surface2.get_width() + 10)
                            if event.key == pygame.K_RETURN:
                                Iniciar_Jogo.jogar(screen,screen_width,screen_height)
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                       # user_text2 = user_text[:-1]
                    else:
                        user_text += event.unicode
                       # user_text2 += event.unicode
                    
            # Dar blit na tela                
            screen.blit(background_image, (0,0))
            screen.blit(button_escrever_text, button_escrever_pos)
            screen.blit(button_escrever_text2, button_escrever_pos2)
            pygame.draw.rect(screen, vermelho, (670, 420, 200, 85), 50)
            screen.blit(button_voltar_text, button_voltar_pos)
            text_surface = font.render(user_text, True, preto) 
            screen.blit(text_surface, (input_rect.x + 200, input_rect.y + 30 + dy))
            input_rect.w = max(435, text_surface.get_width() + 10)
            pygame.display.update()
            if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    pygame.QUIT
            if area_sair_escolhaNomes2.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    pygame.QUIT
            pygame.display.update()

            