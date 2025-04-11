import pygame
import sys
import random

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Definição das dimensões da janela
WIDTH, HEIGHT = 900, 700

# Definição das dimensões da tabela
TABLE_WIDTH = 800
TABLE_HEIGHT = 400
CELL_WIDTH = TABLE_WIDTH // 4
CELL_HEIGHT = TABLE_HEIGHT // 3

# Definição dos jogadores
PLAYER_HUMAN = 1
PLAYER_BOT = 2

pygame.init()

# Definição da janela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Semáforo')

# Tabela de botões
table_rect = pygame.Rect((WIDTH - TABLE_WIDTH) // 2,
                         (HEIGHT - TABLE_HEIGHT) // 2,
                         TABLE_WIDTH, TABLE_HEIGHT)
button_rects = []
button_colors = [GRAY] * 12
current_player = PLAYER_HUMAN

for i in range(4):
    for j in range(3):
        button_rects.append(pygame.Rect(table_rect.left + i * CELL_WIDTH,
                                        table_rect.top + j * CELL_HEIGHT,
                                        CELL_WIDTH, CELL_HEIGHT))

# Função para verificar se há uma linha de 3 cores iguais
def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [9, 10, 11],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [4, 7, 10],
        [5, 8, 11],
        [0, 4, 8],
        [3, 7, 11],
        [2, 4, 6],
        [5, 7, 9],
    ]

    for combination in winning_combinations:
        colors = [button_colors[i] for i in combination]
        if colors == [GREEN] * 3 or colors == [YELLOW] * 3 or colors == [RED] * 3:
            return True

    return False

# Função para realizar a jogada do jogador humano
def make_human_move():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for index, rect in enumerate(button_rects):
                if rect.collidepoint(event.pos):
                    if button_colors[index] == GRAY:
                        button_colors[index] = GREEN
                    elif button_colors[index] == GREEN:
                        button_colors[index] = YELLOW
                    elif button_colors[index] == YELLOW:
                        button_colors[index] = RED
                    return True

    return False

# Função para realizar a jogada do jogador bot
def make_bot_move():
    available_moves = [index for index, color in enumerate(button_colors) if color == GRAY or color == GREEN or color == YELLOW]
    if available_moves:
        move = random.choice(available_moves)
        if button_colors[move] == GRAY:
            button_colors[move] = GREEN
        elif button_colors[move] == GREEN:
            button_colors[move] = YELLOW
        elif button_colors[move] == YELLOW:
            button_colors[move] = RED

    return True

# Loop principal
running = True
while running:
    if current_player == PLAYER_HUMAN:
        move_made = make_human_move()
    else:
        move_made = make_bot_move()

    if move_made:
        if check_winner():
            if current_player == PLAYER_HUMAN:
                print("Jogador humano venceu!")
            else:
                print("Jogador bot venceu!")
            running = False

        if current_player == PLAYER_HUMAN:
            current_player = PLAYER_BOT
        else:
            current_player = PLAYER_HUMAN

    # Desenho da tabela de botões
    window.fill(BLACK)
    pygame.draw.rect(window, GRAY, table_rect)
    for index, rect in enumerate(button_rects):
        color = button_colors[index]
        pygame.draw.rect(window, color, rect)
        pygame.draw.rect(window, BLACK, rect, 1)

    # Atualizar a janela
    pygame.display.update()

# Finalizar o Pygame
pygame.quit()
sys.exit()





