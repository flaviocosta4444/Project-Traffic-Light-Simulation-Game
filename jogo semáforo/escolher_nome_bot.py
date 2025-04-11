import pygame
from teste_pvb import Iniciar_Jogo_Bot

class Escolher_Nome_Bot:
    def escolhaNomeBot(screen,screen_width,screen_height):

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
        input_rect = pygame.Rect(100, 80, 435, 100)
        area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
        user_text = ''

        # Definir os textos dos botões
        button_escrever_text = font.render("Escreva o seu nome:", True, preto)
        button_voltar_text = font2.render("Voltar", True, preto)

        button_escrever_pos = button_escrever_text.get_rect(center=(120, 120))
        button_voltar_pos = button_voltar_text.get_rect(center=(770, 470))

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
                        nome=user_text
                        ficheiro_nome = open("nomes.txt", "w")
                        ficheiro_nome.write(nome)
                        ficheiro_nome.close()
                        Iniciar_Jogo_Bot.jogarbot(screen,screen_width,screen_height)
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    

            # Dar blit na tela                
            screen.blit(background_image, (0,0))
            screen.blit(button_escrever_text, button_escrever_pos)
            pygame.draw.rect(screen, vermelho, (670, 420, 200, 85), 50)
            screen.blit(button_voltar_text, button_voltar_pos)
            text_surface = font.render(user_text, True, (0, 0, 0)) 
            screen.blit(text_surface, (input_rect.x + 130, input_rect.y + 30))
            input_rect.w = max(435, text_surface.get_width() + 10)
            pygame.display.update()
            if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    pygame.QUIT
            pygame.display.update()