import pygame
import random
import sys

class Iniciar_Jogo_Bot:
    def jogarbot(screen,screen_width,screen_height):
        
        # Carrega o background
        background_image = pygame.image.load(r"C:\Users\FLÁVIOMIGUELGOMESCOS\Desktop\imagens_semáforo\imagem_menu.png").convert()  
        # Redimensionar imagem
        background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))
        
        # Definição das cores
        black = (0, 0, 0)
        branco = (255, 255, 255)
        cinza = (128, 128, 128)
        verde = (0, 255, 0)
        amarelo = (255, 255, 0)
        vermelho = (255, 0, 0)

        # Definir fonte
        font = pygame.font.SysFont(None, 40)

        # Definir Cores
        preto = (0, 0, 0)

        # Definir os textos dos botões
        button_voltar_text = font.render("Voltar", True, cinza)

        # Definir as posições dos botões
        button_voltar_pos = button_voltar_text.get_rect(center=(1375, 790))

        # Definição das dimensões da tabela
        tabela_width = 750
        tabela_height = 400
        celula_widht = tabela_width // 4
        celula_height = tabela_height // 3

        # Definição dos jogadores
        jogador_humano = 1
        jogador_bot = 2

        # Tabela de botões
        table_rect = pygame.Rect((screen_width - tabela_width) // 2,
                         (screen_height - tabela_height) // 2,
                         tabela_width, tabela_height)
        button_rects = []
        button_colors = [cinza] * 12
        jogador_atual = jogador_humano

        for i in range(4):
            for j in range(3):
                button_rects.append(pygame.Rect(table_rect.left + i * celula_widht,
                                                table_rect.top + j * celula_height,
                                                celula_widht, celula_height))
                

        # Função para verificar se há uma linha de 3 cores iguais
        def vencedor():
            winning_combinations = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [9, 10, 11],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [3, 7, 11],
                [0, 4, 8],
                [2, 4, 6],
                [3, 6, 9],
                [4, 7, 10],
                [5, 8, 11],
                [5, 7, 9]
            ]

            for combination in winning_combinations:
                colors = [button_colors[i] for i in combination]
                if colors == [verde] * 3 or colors == [amarelo] * 3 or colors == [vermelho] * 3:
                    return True

            return False

        # Função para realizar a jogada do jogador humano
        def jogada_jogador_humano():
            button_escolher_text = font.render("É a vez do Jogador Humano", True, preto)
            button_escolher_pos = button_escolher_text.get_rect(center=(770, 190))
            screen.blit(button_escolher_text, button_escolher_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for index, rect in enumerate(button_rects):
                        if rect.collidepoint(event.pos):
                            if button_colors[index] == cinza:
                                button_colors[index] = verde
                            elif button_colors[index] == verde:
                                button_colors[index] = amarelo
                            elif button_colors[index] == amarelo:
                                button_colors[index] = vermelho
                            elif button_colors[index] != vermelho:
                                return True
                            return True
                
            pygame.display.update()

            return False

        # Função para realizar a jogada do jogador bot
        def jogada_jogador_bot():
            button_escolher_text = font.render("É a vez do Bot", True, preto)
            button_escolher_pos = button_escolher_text.get_rect(center=(770, 190))
            screen.blit(button_escolher_text, button_escolher_pos)
            pygame.display.update()
            available_moves = [index for index, color in enumerate(button_colors) if color == cinza or color == verde or color == amarelo]
            if available_moves:
                move = random.choice(available_moves)
                if button_colors[move] == cinza:
                    button_colors[move] = verde
                elif button_colors[move] == verde:
                    button_colors[move] = amarelo
                elif button_colors[move] == amarelo:
                    button_colors[move] = vermelho

            return True

        # Loop principal
        running = True
        while running:
            if jogador_atual == jogador_humano:
                jogada_feita = jogada_jogador_humano()
            else:
                jogada_feita = jogada_jogador_bot()

            if jogada_feita:
                if vencedor():
                    if jogador_atual == jogador_humano:
                        button_escolher_text = font.render("O Jogador Humano ganhou", True, preto)
                        button_escolher_pos = button_escolher_text.get_rect(center=(770, 300))
                        screen.blit(button_escolher_text, button_escolher_pos)
                        pygame.display.update()
                    else:
                        button_escolher_text = font.render("O Jogador Bot ganhou", True, preto)
                        button_escolher_pos = button_escolher_text.get_rect(center=(770, 300))
                        screen.blit(button_escolher_text, button_escolher_pos)
                        pygame.display.update()
                    
                    pygame.time.delay(3000)
                    running = False

                if jogador_atual == jogador_humano:
                    jogador_atual = jogador_bot
                else:
                    jogador_atual = jogador_humano
                
            # Verificar se o clique foi no botão voltar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_voltar_pos.collidepoint(mouse_pos):
                        return

            # Dar blit na tela
            screen.blit(background_image, (0, 0))

            pygame.draw.rect(screen, branco, (1250, 750, 250, 80), 50)
            screen.blit(button_voltar_text, button_voltar_pos)

            # Desenho da tabela de botões
            pygame.draw.rect(screen, cinza, table_rect)
            for index, rect in enumerate(button_rects):
                color = button_colors[index]
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, black, rect, 1)

            # Atualizar a janela
            pygame.display.update()

        # Finalizar o Pygame
        pygame.quit()
        sys.exit()