import pygame

class Regras:
    def mostrar_regras(screen,screen_width,screen_height):
        # Carrega o background
        background_image = pygame.image.load(r"C:\Users\FLÁVIOMIGUELGOMESCOS\Desktop\imagens_semáforo\regras.png").convert()  
        # Redimensionar imagem
        background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))
        
        # Definir fonte 
        font_menu = pygame.font.SysFont(None, 40)

        # Definir cores
        preto = (0, 0, 0)
        amarelo = (255, 255, 50)

        # Definir os textos dos botões
        button_voltar_text = font_menu.render("Voltar", True, amarelo)

        # Definir as posições dos botões
        button_voltar_pos = button_voltar_text.get_rect(center=(1375, 790))

        # Loop principal do jogo
        running = True
        while running:
            # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar se o clique foi em um dos botões
                    mouse_pos = pygame.mouse.get_pos()
                    if button_voltar_pos.collidepoint(mouse_pos):
                        return    

            # Desenhar a imagem de fundo na tela
            screen.blit(background_image, (0, 0))

            # Desenhar o botão voltar na tela
            pygame.draw.rect(screen, preto, (1250, 750, 250, 80), 50)
            screen.blit(button_voltar_text, button_voltar_pos)

            # Atualizar a tela
            pygame.display.update()

# Encerrar o Pygame
pygame.quit()