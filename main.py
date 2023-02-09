import pygame
import random
import pickle
import os.path
import requests

pos = [0, 0]

b = []
pygame.init()

main_menu = True

kish_sound = pygame.mixer.Sound("ding.wav")
kish_sound.set_volume(0.9)

myfont = pygame.font.SysFont("Comic Sans MS", 20)
label = myfont.render("main menu", 1, (200, 70, 30))

resume_game_botton = False

menu_font = pygame.font.SysFont("Broadway", 45)
end_game_font = pygame.font.SysFont("Broadway", 90)
save_and_quit_font = pygame.font.SysFont("Broadway", 30)

maat_value = False

black = 0, 0, 0
white = 255, 255, 255
white_movement = (100, 100, 200)
black_movement = (100, 200, 100)

x_click = 0
y_click = 0
x = 0
y = 0
current_mouse_pos_x = 0
current_mouse_pos_y = 0

pygame.display.set_caption('chess')

board_colors = [(80, 80, 80), (255, 255, 255)]

screen = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()

turn = [False, True, False]
turn_index = 0

tile_size = 60
width, height = 480, 480

background = pygame.Surface((width, height))


class piece:
    # life = True
    show = True

    def __init__(self, x, y, rank, color):
        self.x = x
        self.y = y
        self.rank = rank
        self.color = color
        self.life = True

if os.path.isfile("database1"):
    database1 = open("database1", "rb")
    database1 = database1.read()
    database1 = pickle.loads(database1)
    pieces = database1
else:
    pieces = [piece(0, 0, "r", "black"), piece(1, 0, "h", "black"), piece(2, 0, "b", "black"), piece(3, 0, "q", "black"), piece(4, 0, "k", "black"), piece(5, 0, "b", "black"), piece(6, 0, "h", "black"), piece(7, 0, "r", "black"),
         piece(0, 1, "p", "black"), piece(1, 1, "p", "black"), piece(2, 1, "p", "black"), piece(3, 1, "p", "black"), piece(4, 1, "p", "black"), piece(5, 1, "p", "black"), piece(6, 1, "p", "black"), piece(7, 1, "p", "black"),
         piece(0, 7, "r", "white"), piece(1, 7, "h", "white"), piece(2, 7, "b", "white"), piece(3, 7, "q", "white"), piece(4, 7, "k", "white"), piece(5, 7, "b", "white"), piece(6, 7, "h", "white"), piece(7, 7, "r", "white"),
         piece(0, 6, "p", "white"), piece(1, 6, "p", "white"), piece(2, 6, "p", "white"), piece(3, 6, "p", "white"), piece(4, 6, "p", "white"), piece(5, 6, "p", "white"), piece(6, 6, "p", "white"), piece(7, 6, "p", "white")]

if os.path.isfile("database2"):
    database2 = open("database2", "rb")
    database2 = database2.read()
    database2 = pickle.loads(database2)
    turn_index = database2
    resume_value = True
else:
    turn_index = 0
    resume_value = False


def chess_board(width, height, tile_size, color):

    counter = 0
    for y in range(0, height, tile_size):
        counter += 1
        if counter > 1:
            counter = 0
        for x in range(0, width, tile_size):
            counter += 1
            if counter > 1:
                counter = 0

            if color == (80, 80, 80) or color == (255, 255, 255):
                if color == (80, 80, 80):
                    counter = 0
                else:
                    counter = 1

            rect = (x, y, tile_size, tile_size)
            pygame.draw.rect(background, board_colors[counter], rect)


def recognize_pices():
    for i in range(len(pieces)):
        if pieces[i].rank == "r":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_r.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_r.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))
        elif pieces[i].rank == "h":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_h.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_h.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))
        elif pieces[i].rank == "b":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_b.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_b.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))
        elif pieces[i].rank == "q":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_q.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_q.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))
        elif pieces[i].rank == "k":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_k.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_k.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))
        elif pieces[i].rank == "p":
            if pieces[i].color == "white" and pieces[i].life:
                igm = pygame.image.load("white_p.png")
                screen.blit(igm, (pieces[i].x * tile_size, pieces[i].y * tile_size))
            elif pieces[i].color == "black" and pieces[i].life:
                img = pygame.image.load("black_p.png")
                screen.blit(img, (pieces[i].x*tile_size, pieces[i].y*tile_size))


def empty_tile(x, y):
    counter = 0
    for i in range(len(pieces)):
        if pieces[i].x == x and pieces[i].y == y:
            counter += 1
    if counter > 0:
        return False
    else:
        return True


def piece_index(x, y):

    for i in range(len(pieces)):
        if pieces[i].x == x and pieces[i].y == y:
            break
    return i


def show_movments(x_pos, y_pos):
    for i in range(len(pieces)):
        if pieces[i].rank == "p" and pieces[i].x == x_pos and pieces[i].y == y_pos and pieces[i].color == "black":  # سرباز مشکی"
                if empty_tile(x_pos, y_pos + 1):
                    pygame.draw.rect(screen, black_movement, (x_pos * tile_size, y_pos * tile_size + tile_size, tile_size, tile_size), 4)
                if empty_tile(x_pos, y_pos + 2):
                    if pieces[i].y == 1:
                        pygame.draw.rect(screen, black_movement, (x_pos * tile_size, y_pos * tile_size + 2 * tile_size, tile_size, tile_size), 4)
                if not empty_tile(x_pos + 1, y_pos + 1) and pieces[piece_index(x_pos + 1, y_pos + 1)].color != pieces[
                    i].color and x_pos+1 <= 7:
                    pygame.draw.rect(screen, black_movement, (x_pos * tile_size + tile_size, y_pos * tile_size + tile_size, tile_size, tile_size), 4)

                if not empty_tile(x_pos - 1, y_pos + 1) and pieces[piece_index(x_pos - 1, y_pos + 1)].color != pieces[
                    i].color and x_pos - 1 >= 0:
                    pygame.draw.rect(screen, black_movement, (x_pos * tile_size - tile_size, y_pos * tile_size + tile_size, tile_size, tile_size), 4)

        elif pieces[i].rank == "p" and pieces[i].x == x_pos and pieces[i].y == y_pos and pieces[i].color == "white":
                if empty_tile(x_pos, y_pos - 1):
                    pygame.draw.rect(screen, white_movement, (x_pos * tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)
                if empty_tile(x_pos, y_pos - 2):
                    if pieces[i].y == 6:
                        pygame.draw.rect(screen, white_movement, (x_pos * tile_size, y_pos * tile_size - 2 * tile_size, tile_size, tile_size), 4)
                if not empty_tile(x_pos + 1, y_pos - 1) and pieces[piece_index(x_pos + 1, y_pos - 1)].color != pieces[
                    i].color and x_pos + 1 <= 7:
                    pygame.draw.rect(screen, white_movement, (x_pos * tile_size + tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)

                if not empty_tile(x_pos - 1, y_pos - 1) and pieces[piece_index(x_pos - 1, y_pos - 1)].color != pieces[
                    i].color and x_pos - 1 >= 0:
                    pygame.draw.rect(screen, white_movement, (x_pos * tile_size - tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)

        elif pieces[i].rank == "r" and pieces[i].x == x_pos and pieces[i].y == y_pos and pieces[i].life:
                if pieces[i].color == "black":

                    n = 1
                    while n:  # down
                        if y_pos + n > 7:
                            break
                        if empty_tile(x_pos, y_pos + n):
                            pygame.draw.rect(screen, black_movement, (
                            x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 4)
                        else:
                            if pieces[piece_index(x_pos, y_pos + n)].color != pieces[i].color:
                                pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                    n = 1
                    while n:  # up
                        if y_pos - n < 0:
                            break
                        if empty_tile(x_pos, y_pos - n):
                            pygame.draw.rect(screen, black_movement, (
                            x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 4)
                        else:
                            if pieces[piece_index(x_pos, y_pos - n)].color != pieces[i].color:
                                pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                    n = 1
                    while n:  # right
                        if x_pos + n > 7:
                            break
                        if empty_tile(x_pos + n, y_pos):
                            pygame.draw.rect(screen, black_movement, (
                            x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                        else:
                            if pieces[piece_index(x_pos + n, y_pos)].color != pieces[i].color:
                                pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1


                    n = 1
                    while n:  # left
                        if x_pos - n < 0:
                            break
                        if empty_tile(x_pos - n, y_pos):
                            pygame.draw.rect(screen, black_movement, (
                            x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                        else:
                            if pieces[piece_index(x_pos - n, y_pos)].color != pieces[i].color:
                                pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                elif pieces[i].color == "white":

                    n = 1
                    while n:  # down
                        if y_pos + n > 7:
                            break
                        if empty_tile(x_pos, y_pos + n):
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 4)
                        else:
                            if pieces[piece_index(x_pos, y_pos + n)].color != pieces[i].color:
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                    n = 1
                    while n:  # up
                        if y_pos - n < 0:
                            break
                        if empty_tile(x_pos, y_pos - n):
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 4)
                        else:
                            if pieces[piece_index(x_pos, y_pos - n)].color != pieces[i].color:
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                    n = 1
                    while n:  # right
                        if x_pos + n > 7:
                            break
                        if empty_tile(x_pos + n, y_pos):
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                        else:
                            if pieces[piece_index(x_pos + n, y_pos)].color != pieces[i].color:
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1

                    n = 1
                    while n:  # left
                        if x_pos - n < 0:
                            break
                        if empty_tile(x_pos - n, y_pos):
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                        else:
                            if pieces[piece_index(x_pos - n, y_pos)].color != pieces[i].color:
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 4)
                                break

                            else:
                                break
                        n += 1
# ----------------------------------------------------------------------------------------------------------------------
        elif pieces[i].rank == "b" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                n = 1
                while n:  # down right
                    if x_pos + n > 7:
                        break
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos + n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size), 4)

                    else:
                        if pieces[piece_index(x_pos + n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size), 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size), 4)
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if x_pos + n > 7:
                        break
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos + n, y_pos - n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size), 4)
                    else:
                        if pieces[piece_index(x_pos + n, y_pos - n)].color != pieces[i].color:

                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size), 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size), 4)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up left
                    if y_pos + n > 7:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos + n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size),
                                             4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size),
                                             4)
                    else:
                        if pieces[piece_index(x_pos - n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size),
                                                 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size),
                                                 4)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if y_pos - n < 0:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos - n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size),
                                             4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size),
                                             4)
                    else:
                        if pieces[piece_index(x_pos - n, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size),
                                                 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size),
                                                 4)
                            break

                        else:
                            break
                    n += 1
#----------------------------------------------------------------------------------------------------------------------
        elif pieces[i].rank == "h" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                if x_pos + 1 < 8 and y_pos + 2 < 8:
                    if empty_tile(x_pos + 1, y_pos + 2) or pieces[piece_index(x_pos + 1, y_pos + 2)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size + 1*tile_size, y_pos *tile_size + 2*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size + 1 * tile_size, y_pos*tile_size + 2 * tile_size, tile_size, tile_size), 4)

                if x_pos - 1 >= 0 and y_pos + 2 < 8:
                    if empty_tile(x_pos - 1, y_pos + 2) or pieces[piece_index(x_pos - 1, y_pos + 2)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size - 1*tile_size, y_pos *tile_size + 2*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size - 1 * tile_size, y_pos*tile_size + 2 * tile_size, tile_size, tile_size), 4)

                if x_pos + 2 < 8 and y_pos - 1 >= 0:
                    if empty_tile(x_pos + 2, y_pos - 1) or pieces[piece_index(x_pos + 2, y_pos - 1)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size + 2*tile_size, y_pos *tile_size - 1*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size + 2 * tile_size, y_pos*tile_size - 1 * tile_size, tile_size, tile_size), 4)

                if x_pos + 2 < 8 and y_pos + 1 < 8:
                    if empty_tile(x_pos + 2, y_pos + 1) or pieces[piece_index(x_pos + 2, y_pos + 1)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size + 2*tile_size, y_pos *tile_size + 1*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size + 2 * tile_size, y_pos*tile_size + 1 * tile_size, tile_size, tile_size), 4)

                if x_pos + 1 < 8 and y_pos -2 >= 0:
                    if empty_tile(x_pos + 1, y_pos - 2) or pieces[piece_index(x_pos + 1, y_pos - 2)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size + 1*tile_size, y_pos *tile_size - 2*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size + 1 * tile_size, y_pos*tile_size - 2 * tile_size, tile_size, tile_size), 4)

                if x_pos - 1 >= 0 and y_pos - 2 >= 0:
                    if empty_tile(x_pos - 1, y_pos - 2) or pieces[piece_index(x_pos - 1, y_pos - 2)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                            x_pos * tile_size - 1 * tile_size, y_pos * tile_size - 2 * tile_size, tile_size, tile_size),
                                             4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                            x_pos * tile_size - 1 * tile_size, y_pos * tile_size - 2 * tile_size, tile_size, tile_size),
                                             4)

                if x_pos - 2 >= 0 and y_pos - 1 >= 0:
                    if empty_tile(x_pos - 2, y_pos - 1) or pieces[piece_index(x_pos - 2, y_pos - 1)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size - 2*tile_size, y_pos *tile_size - 1*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size - 2 * tile_size, y_pos*tile_size - 1 * tile_size, tile_size, tile_size), 4)

                if x_pos - 2 >= 0 and y_pos + 1 < 8:
                    if empty_tile(x_pos - 2, y_pos + 1) or pieces[piece_index(x_pos - 2, y_pos + 1)].color != pieces[i].color:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos * tile_size - 2*tile_size, y_pos *tile_size + 1*tile_size, tile_size, tile_size), 4)
                        elif pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos * tile_size - 2 * tile_size, y_pos*tile_size + 1 * tile_size, tile_size, tile_size), 4)

        elif pieces[i].rank == "q" and pieces[i].x == x_pos and pieces[i].y == y_pos:

                n = 1
                while n:  # down
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos, y_pos + n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 5)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 5)
                    else:
                        if pieces[piece_index(x_pos, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 5)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size, y_pos * tile_size + n * tile_size, tile_size, tile_size), 5)
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos, y_pos - n):
                        if pieces[i].color == "black":
                             pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 5)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 5)
                    else:
                        if pieces[piece_index(x_pos, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 5)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size, y_pos * tile_size - n * tile_size, tile_size, tile_size), 5)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # right
                    if x_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)

                    else:
                        if pieces[piece_index(x_pos + n, y_pos)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # left
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)

                    else:
                        if pieces[piece_index(x_pos - n, y_pos)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size, tile_size, tile_size), 5)
                            break

                        else:
                            break
                    n += 1

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                n = 1
                while n:  # down right
                    if x_pos + n > 7:
                        break
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos + n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size), 4)

                    else:
                        if pieces[piece_index(x_pos + n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size), 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size), 4)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if x_pos + n > 7:
                        break
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos + n, y_pos - n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size), 4)
                    else:
                        if pieces[piece_index(x_pos + n, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size), 4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size), 4)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # down left
                    if y_pos + n > 7:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos + n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size),
                                                4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                tile_size),
                                                4)
                    else:
                        if pieces[piece_index(x_pos - n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size),
                                                    4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size, tile_size,
                                    tile_size),
                                                    4)
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if y_pos - n < 0:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos - n):
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size),
                                                4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (
                                x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                tile_size),
                                              4)
                    else:
                        if pieces[piece_index(x_pos - n, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                pygame.draw.rect(screen, black_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size),
                                                    4)
                            if pieces[i].color == "white":
                                pygame.draw.rect(screen, white_movement, (
                                    x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size, tile_size,
                                    tile_size),
                                                    4)
                            break

                        else:
                            break
                    n += 1

        elif pieces[i].rank == "k" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                if empty_tile(x_pos + 1, y_pos + 1) or pieces[piece_index(x_pos + 1, y_pos + 1)].color != pieces[i].color:
                    if x_pos + 1 < 8 and y_pos + 1 < 8:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement, (x_pos*tile_size + 1*tile_size,y_pos*tile_size + 1*tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement, (x_pos*tile_size + 1*tile_size,y_pos*tile_size + 1*tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos, y_pos + 1) or pieces[piece_index(x_pos, y_pos + 1)].color != pieces[i].color:
                    if y_pos + 1 < 8:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size,y_pos*tile_size + 1*tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size, y_pos * tile_size + 1 * tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos + 1, y_pos) or pieces[piece_index(x_pos + 1, y_pos)].color != pieces[i].color:
                    if x_pos + 1 < 8:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size + tile_size, y_pos*tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size + tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos + 1, y_pos - 1) or pieces[piece_index(x_pos + 1, y_pos - 1)].color != pieces[i].color:
                    if x_pos + 1 < 8 and y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size + tile_size, y_pos*tile_size - tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size + tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos, y_pos - 1) or pieces[piece_index(x_pos, y_pos - 1)].color != pieces[i].color:
                    if y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size, y_pos*tile_size - tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos - 1, y_pos - 1) or pieces[piece_index(x_pos - 1, y_pos - 1)].color != pieces[i].color:
                    if x_pos - 1 >= 0 and y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size - tile_size, y_pos*tile_size - tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size - tile_size, y_pos * tile_size - tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos - 1, y_pos) or pieces[piece_index(x_pos - 1, y_pos)].color != pieces[i].color:
                    if x_pos - 1 >= 0:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size - tile_size, y_pos*tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size - tile_size, y_pos * tile_size, tile_size, tile_size), 4)

                if empty_tile(x_pos - 1, y_pos + 1) or pieces[piece_index(x_pos - 1, y_pos + 1)].color != pieces[i].color:
                    if x_pos - 1 >= 0 and y_pos + 1 < 8:
                        if pieces[i].color == "black":
                            pygame.draw.rect(screen, black_movement,
                                         (x_pos * tile_size - tile_size, y_pos*tile_size + tile_size, tile_size, tile_size), 4)
                        if pieces[i].color == "white":
                            pygame.draw.rect(screen, white_movement,
                                         (x_pos * tile_size - tile_size, y_pos * tile_size + tile_size, tile_size, tile_size), 4)


def list_movement(x_pos, y_pos):
    return_list = []
    for i in range(len(pieces)):
      #  for j in range(len(pieces)):
        if pieces[i].rank == "p" and pieces[i].x == x_pos and pieces[i].y == y_pos and pieces[i].color == "black":   # سرباز مشکی"
                if empty_tile(x_pos, y_pos + 1):
                    return_list.extend([(x_pos * tile_size, y_pos * tile_size + tile_size)])
                if empty_tile(x_pos, y_pos + 2):
                    if pieces[i].y == 1:
                        return_list.extend([(x_pos * tile_size, y_pos * tile_size+2*tile_size)])
                if not empty_tile(x_pos + 1, y_pos + 1) and pieces[piece_index(x_pos + 1, y_pos + 1)].color != pieces[i].color:
                    return_list.extend([(x_pos * tile_size + tile_size, y_pos * tile_size + tile_size)])

                if not empty_tile(x_pos - 1, y_pos + 1) and pieces[piece_index(x_pos - 1, y_pos + 1)].color != pieces[i].color:
                    return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size + tile_size)])

        elif pieces[i].rank == "p" and pieces[i].x == x_pos and pieces[i].y == y_pos and pieces[i].color == "white":
                if empty_tile(x_pos, y_pos - 1):
                    return_list.extend([(x_pos * tile_size, y_pos * tile_size - tile_size)])
                if empty_tile(x_pos, y_pos - 2):
                    if pieces[i].y == 6:
                        return_list.extend([(x_pos * tile_size, y_pos * tile_size-2*tile_size)])
                if not empty_tile(x_pos + 1, y_pos - 1) and pieces[piece_index(x_pos + 1, y_pos - 1)].color != pieces[i].color:
                    return_list.extend([(x_pos * tile_size + tile_size, y_pos * tile_size - tile_size)])

                if not empty_tile(x_pos - 1, y_pos - 1) and pieces[piece_index(x_pos - 1, y_pos - 1)].color != pieces[i].color:
                    return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size - tile_size)])

        elif pieces[i].rank == "r" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                n = 1
                while n:  # down
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos, y_pos + n):
                        return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos, y_pos + n)].color != pieces[i].color:
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos, y_pos - n):
                        return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos, y_pos - n)].color != pieces[i].color:
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # right
                    if x_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos):
                        return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])
                    else:
                        if pieces[piece_index(x_pos + n, y_pos)].color != pieces[i].color:
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])
                            break
                        else:
                            break
                    n += 1


                n = 1
                while n:  # left
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos):
                        return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])

                    else:
                        if pieces[piece_index(x_pos - n, y_pos)].color != pieces[i].color:
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])
                            break
                        else:
                            break
                    n += 1
              #----------------------------------------------------------------------------------------
        elif pieces[i].rank == "b" and pieces[i].x == x_pos and pieces[i].y == y_pos:

                n = 1
                while n:  # down right
                    if y_pos + n > 7:
                        break
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos + n):
                        return_list.extend([(
                            x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])

                    else:
                        if pieces[piece_index(x_pos + n, y_pos + n)].color != pieces[i].color:
                            return_list.extend([(
                                x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if x_pos + n > 7:
                        break
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos + n, y_pos - n):
                        return_list.extend([(
                            x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos + n, y_pos - n)].color != pieces[i].color:
                            return_list.extend([(
                                x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # down left
                    if y_pos + n > 7:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos + n):
                        return_list.extend([(
                            x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos - n, y_pos + n)].color != pieces[i].color:
                            return_list.extend([(
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up left
                    if y_pos - n < 0:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos - n):
                        return_list.extend([(
                            x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos - n, y_pos - n)].color != pieces[i].color:
                            return_list.extend([(
                                x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

        elif pieces[i].rank == "h" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                if x_pos + 1 < 8 and y_pos + 2 < 8:
                    if empty_tile(x_pos + 1, y_pos + 2) or pieces[piece_index(x_pos + 1, y_pos + 2)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size + 1*tile_size, y_pos *tile_size + 2*tile_size)])

                if x_pos - 1 >= 0 and y_pos + 2 < 8:
                    if empty_tile(x_pos - 1, y_pos + 2) or pieces[piece_index(x_pos - 1, y_pos + 2)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size - 1*tile_size, y_pos *tile_size + 2*tile_size)])

                if x_pos + 2 < 8 and y_pos - 1 >= 0:
                    if empty_tile(x_pos + 2, y_pos - 1) or pieces[piece_index(x_pos + 2, y_pos - 1)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size + 2*tile_size, y_pos *tile_size - 1*tile_size)])

                if x_pos + 2 < 8 and y_pos + 1 < 8:
                    if empty_tile(x_pos + 2, y_pos + 1) or pieces[piece_index(x_pos + 2, y_pos + 1)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size + 2*tile_size, y_pos *tile_size + 1*tile_size)])

                if x_pos + 1 < 8 and y_pos -2 >= 0:
                    if empty_tile(x_pos + 1, y_pos - 2) or pieces[piece_index(x_pos + 1, y_pos - 2)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size + 1*tile_size, y_pos *tile_size - 2*tile_size)])

                if x_pos - 1 >= 0 and y_pos - 2 >= 0:
                    if empty_tile(x_pos - 1, y_pos - 2) or pieces[piece_index(x_pos - 1, y_pos - 2)].color != pieces[i].color:
                        return_list.extend([(
                            x_pos * tile_size - 1 * tile_size, y_pos * tile_size - 2 * tile_size)])

                if x_pos - 2 >= 0 and y_pos - 1 >= 0:
                    if empty_tile(x_pos - 2, y_pos - 1) or pieces[piece_index(x_pos - 2, y_pos - 1)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size - 2*tile_size, y_pos *tile_size - 1*tile_size)])

                if x_pos - 2 >= 0 and y_pos + 1 < 8:
                    if empty_tile(x_pos - 2, y_pos + 1) or pieces[piece_index(x_pos - 2, y_pos + 1)].color != pieces[i].color:
                        return_list.extend([(x_pos * tile_size - 2*tile_size, y_pos *tile_size + 1*tile_size)])

        elif pieces[i].rank == "q" and pieces[i].x == x_pos and pieces[i].y == y_pos:

                n = 1
                while n:  # down
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos, y_pos + n):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size + n * tile_size)])
                            break
                        else:
                            break
                    n += 1

                n = 1
                while n:  # up
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos, y_pos - n):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # right
                    if x_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])

                    else:
                        if pieces[piece_index(x_pos + n, y_pos)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # left
                    if x_pos - n < 0:
                         break
                    if empty_tile(x_pos - n, y_pos):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])
                    else:
                        if pieces[piece_index(x_pos - n, y_pos)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size)])
                            break

                        else:
                            break
                    n += 1

                        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                n = 1
                while n:  # down right
                    if x_pos + n > 7:
                        break
                    if y_pos + n > 7:
                        break
                    if empty_tile(x_pos + n, y_pos + n):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])

                    else:
                        if pieces[piece_index(x_pos + n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size + n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if x_pos + n > 7:
                        break
                    if y_pos - n < 0:
                        break
                    if empty_tile(x_pos + n, y_pos - n):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos + n, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size + n * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # down left
                    if y_pos + n > 7:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos + n):
                        if pieces[i].color == "black":
                            return_list.extend([(
                                x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos - n, y_pos + n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size + n * tile_size)])
                            break

                        else:
                            break
                    n += 1

                n = 1
                while n:  # up right
                    if y_pos - n < 0:
                        break
                    if x_pos - n < 0:
                        break
                    if empty_tile(x_pos - n, y_pos - n):
                        if pieces[i].color == "black":
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                        if pieces[i].color == "white":
                            return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                    else:
                        if pieces[piece_index(x_pos - n, y_pos - n)].color != pieces[i].color:
                            if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                            if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - n * tile_size, y_pos * tile_size - n * tile_size)])
                            break

                        else:
                            break
                    n += 1

        elif pieces[i].rank == "k" and pieces[i].x == x_pos and pieces[i].y == y_pos:
                if empty_tile(x_pos + 1, y_pos + 1) or pieces[piece_index(x_pos + 1, y_pos + 1)].color != pieces[i].color:
                    if x_pos + 1 < 8 and y_pos + 1 < 8:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos*tile_size + 1*tile_size,y_pos*tile_size + 1*tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos*tile_size + 1*tile_size,y_pos*tile_size + 1*tile_size)])

                if empty_tile(x_pos, y_pos + 1) or pieces[piece_index(x_pos, y_pos + 1)].color != pieces[i].color:
                    if y_pos + 1 < 8:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size,y_pos*tile_size + 1*tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size + 1 * tile_size)])

                if empty_tile(x_pos + 1, y_pos) or pieces[piece_index(x_pos + 1, y_pos)].color != pieces[i].color:
                    if x_pos + 1 < 8:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size + tile_size, y_pos*tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size + tile_size, y_pos * tile_size)])

                if empty_tile(x_pos + 1, y_pos - 1) or pieces[piece_index(x_pos + 1, y_pos - 1)].color != pieces[i].color:
                    if x_pos + 1 < 8 and y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size + tile_size, y_pos*tile_size - tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size + tile_size, y_pos * tile_size - tile_size)])

                if empty_tile(x_pos, y_pos - 1) or pieces[piece_index(x_pos, y_pos - 1)].color != pieces[i].color:
                    if y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size, y_pos*tile_size - tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size, y_pos * tile_size - tile_size)])

                if empty_tile(x_pos - 1, y_pos - 1) or pieces[piece_index(x_pos - 1, y_pos - 1)].color != pieces[i].color:
                    if x_pos - 1 >= 0 and y_pos - 1 >= 0:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos*tile_size - tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size - tile_size)])

                if empty_tile(x_pos - 1, y_pos) or pieces[piece_index(x_pos - 1, y_pos)].color != pieces[i].color:
                    if x_pos - 1 >= 0:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size)])

                if empty_tile(x_pos - 1, y_pos + 1) or pieces[piece_index(x_pos - 1, y_pos + 1)].color != pieces[i].color:
                    if x_pos - 1 >= 0 and y_pos + 1 < 8:
                        if pieces[i].color == "black":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos*tile_size + tile_size)])
                        if pieces[i].color == "white":
                                return_list.extend([(x_pos * tile_size - tile_size, y_pos * tile_size + tile_size)])

    return return_list


def kish(color):
    list = []
    for i in range(len(pieces)):
        if pieces[i].color != color:
            list.extend(list_movement(pieces[i].x, pieces[i].y))
    if color == "black":
        if (pieces[4].x * tile_size, pieces[4].y *tile_size) in list:
            return True
        else:
            return False
    elif color == "white":
        if (pieces[20].x * tile_size, pieces[20].y * tile_size) in list:
            return True
        else:
            return False


def kish_pos(x_pos, y_pos, color):
    list = []
    for i in range(len(pieces)):
        if pieces[i].color != color:
            list.extend(list_movement(pieces[i].x, pieces[i].y))
    if (x_pos*tile_size, y_pos*tile_size) in list:
        return True
    else:
        return False


def show_kish_movement(x, y, color):
    x_pos = 0
    y_pos = 0
    enemy_index = 0
    v = 0
    j = 0
    index = 0

    for h in range(len(pieces)):
        if color == "black":
            if (pieces[4].x * tile_size, pieces[4].y * tile_size) in list_movement(pieces[h].x, pieces[h].y):
                enemy_index = h
                break
        elif color == "white":
            if (pieces[20].x * tile_size, pieces[20].y * tile_size) in list_movement(pieces[h].x, pieces[h].y):
                enemy_index = h
                break
    if (pieces[enemy_index].x * tile_size, pieces[enemy_index].y* tile_size) in list_movement(pieces[piece_index(x, y)].x, pieces[piece_index(x, y)].y):  #اگه بشه مهره کیش داده رو زد
        if pieces[piece_index(x, y)].color == "black":
            pygame.draw.rect(screen, black_movement, (pieces[enemy_index].x *tile_size, pieces[enemy_index].y *tile_size, tile_size, tile_size), 4)
        if pieces[piece_index(x, y)].color == "white":
            pygame.draw.rect(screen, white_movement, (pieces[enemy_index].x * tile_size, pieces[enemy_index].y * tile_size, tile_size, tile_size), 4)

    for i in range(len(pieces)):
        if pieces[i].x == x and pieces[i].y == y and pieces[i].color == color:
            for k in range(len(list_movement(pieces[i].x, pieces[i].y))):

                if pieces[i].rank == "k":

                    if kish_pos(list_movement(pieces[i].x, pieces[i].y)[k][0], list_movement(pieces[i].x, pieces[i].y)[k][1], color):
                        if pieces[enemy_index].color != "black":
                            pygame.draw.rect(screen, black_movement, (
                            list_movement(pieces[i].x, pieces[i].y)[k][0], list_movement(pieces[i].x, pieces[i].y)[k][1],
                            tile_size, tile_size), 4)
                        if pieces[enemy_index].color != "white":
                            pygame.draw.rect(screen, white_movement, (
                            list_movement(pieces[i].x, pieces[i].y)[k][0], list_movement(pieces[i].x, pieces[i].y)[k][1],
                            tile_size, tile_size), 4)
                noh = list_movement(pieces[i].x, pieces[i].y)[k]
                if list_movement(pieces[i].x, pieces[i].y)[k] in list_movement(pieces[enemy_index].x, pieces[enemy_index].y) and pieces[i].rank != "k":
                    v = pieces[i].x
                    j = pieces[i].y
                    index = i
                    (x_pos, y_pos) = noh
                    pieces[i].x = x_pos//tile_size
                    pieces[i].y = y_pos//tile_size
                    break
                else:
                    continue
            break
    if (x_pos, y_pos) != (0, 0):
      if pieces[enemy_index].color != "black":
        if not kish("black"):
            pygame.draw.rect(screen, black_movement, (x_pos, y_pos, tile_size, tile_size), 4)
      if pieces[enemy_index].color != "white":
        if not kish("white"):
            pygame.draw.rect(screen, white_movement, (x_pos, y_pos, tile_size, tile_size), 4)

    pieces[index].x = v
    pieces[index].y = j


def kish_movement(x, y, color):
    return_list = []
    x_pos = 0
    y_pos = 0
    enemy_index = 0
    v = 0
    j = 0
    index = 0

    for h in range(len(pieces)):
        if color == "black":
            if (pieces[4].x * tile_size, pieces[4].y * tile_size) in list_movement(pieces[h].x, pieces[h].y):
                enemy_index = h
                break
        elif color == "white":
            if (pieces[20].x * tile_size, pieces[20].y * tile_size) in list_movement(pieces[h].x, pieces[h].y):
                enemy_index = h
                break
    if (pieces[enemy_index].x * tile_size, pieces[enemy_index].y* tile_size) in list_movement(pieces[piece_index(x, y)].x, pieces[piece_index(x, y)].y):
       # if color == "black":
        return_list.extend([(pieces[enemy_index].x *tile_size, pieces[enemy_index].y *tile_size)])
       # if color == "white":
       #     return_list.extend([(pieces[enemy_index].x * tile_size, pieces[enemy_index].y * tile_size)])

    for i in range(len(pieces)):
        if pieces[i].x == x and pieces[i].y == y and pieces[i].color == color:
            for k in range(len(list_movement(pieces[i].x, pieces[i].y))):
                if pieces[i].rank == "k":
                    if kish_pos(list_movement(pieces[i].x, pieces[i].y)[k][0],list_movement(pieces[i].x, pieces[i].y)[k][1] , color):
                        if pieces[enemy_index].color != "black":
                            return_list.extend([(
                            list_movement(pieces[i].x, pieces[i].y)[k][0], list_movement(pieces[i].x, pieces[i].y)[k][1])])
                        if pieces[enemy_index].color != "white":
                            return_list.extend([(
                            list_movement(pieces[i].x, pieces[i].y)[k][0], list_movement(pieces[i].x, pieces[i].y)[k][1])])
                noh = list_movement(pieces[i].x, pieces[i].y)[k]
                if list_movement(pieces[i].x, pieces[i].y)[k] in list_movement(pieces[enemy_index].x, pieces[enemy_index].y):
                    v = pieces[i].x
                    j = pieces[i].y
                    index = i
                    (x_pos, y_pos) = noh
                    pieces[i].x = x_pos//tile_size
                    pieces[i].y = y_pos//tile_size
                    break
                else:
                    continue
            break
    if (x_pos, y_pos) != (0, 0):
        if pieces[enemy_index].color != "black" and not kish("black") or pieces[enemy_index].color != "white" and not kish("white"):
            return_list.extend([(x_pos, y_pos)])

    pieces[index].x = v
    pieces[index].y = j
    return return_list


def check_maat(color):
    list = []
    for i in range(len(pieces)):
        if pieces[i].color == color:
            list += kish_movement(pieces[i].x, pieces[i].y, color)
    if list == []:
        return True
    else:
        return False


def move(x_start, y_start, x_goal, y_goal):
    for i in range(len(pieces)):
        if pieces[i].x == x_start and pieces[i].y == y_start:
            if move_permision(start[-2], start[-1], turn_index):
                    pieces[i].x += x_goal - x_start
                    pieces[i].y += y_goal - y_start
                    break


def move_permision(x_pos, y_pos, turn_index):
   # first_x = 0
    #first_y = 0
    index = 0
    for i in range(len(pieces)):
        if pieces[i].x == x_pos and pieces[i].y == y_pos:
            index = i
            break
    first_x = pieces[index].x
    first_y = pieces[index].y

    if turn[turn_index] is True and kish("black") or turn[turn_index] is False and kish("white"):
        return True

    pieces[index].x = 10
    pieces[index].y = 10
    if turn[turn_index] is True and not kish("black") or turn[turn_index] is False and not kish("white"):
        pieces[index].x = first_x
        pieces[index].y = first_y
        return True
    else:
        pieces[index].x = first_x
        pieces[index].y = first_y
        return False


def choose_menu(x, y, x2, y2):
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)

    width = 80
    hight = 40

    width1 = 80
    hight1 = 40

    font1 = pygame.font.SysFont("Comic Sans MS", 25)
    label1 = font1.render("choose what you need", 1, (200, 150, 220))
    label_queen = font1.render("queen", 1, (100, 100, 200))
    label_horse = font1.render("horse", 1, (100, 100, 200))

    if 200 < x < 280 and 100 < y < 140:
        for i in range(len(pieces)):
            if pieces[i].rank == "p" and pieces[i].x < 8:
                if pieces[i].y == 0 or pieces[i].y == 7:
                    pieces[i].rank = "q"

    if 200 < x2 < 280 and 100 < y2 < 140:
        width = 90
        hight = 50

    if 200 < x < 280 and 150 < y < 190:
        for i in range(len(pieces)):
            if pieces[i].rank == "p" and pieces[i].x < 8:
                if pieces[i].y == 0 or pieces[i].y == 7:
                    pieces[i].rank = "h"

    if 200 < x2 < 280 and 150 < y2 < 190:
        width1 = 90
        hight1 = 50

    screen.blit(label1, (200, 50))

    screen.blit(label_queen, (205, 100))
    pygame.draw.rect(screen, (200, 20, 20), (200, 100, width, hight), 5)

    screen.blit(label_horse, (205, 150))
    pygame.draw.rect(screen, (200, 20, 20), (200, 150, width1, hight1), 5)

    pygame.draw.rect(screen, (color1, color2, color3), (180, 20, 300, 200), 10)
    pygame.time.delay(30)

    pygame.display.update()


def moordeh_chin(index):
    for x in range(8, 11):
        for y in range(0, 8):
            if empty_tile(x, y):
                pieces[index].x = x
                pieces[index].y = y
                pieces[index].life = True
                break
            else:
                continue
        break


def main_menu_():

    # choose_color = (130, 200, 200)
    choose_color = (160, 160, 240)
    none_color = (240, 160, 160)

    pygame.draw.rect(screen, (0, 150, 150), (230, 70, 300, 400), 10)
    pygame.draw.rect(screen, (150, 150, 0), (235, 75, 290, 390), 5)

    # if 260 <= current_mouse_pos_x <= 500 and 110 <= current_mouse_pos_y <= 155:
    #     multi_play = menu_font.render("Multi Play", 1, choose_color)
    # else:
    #     multi_play = menu_font.render("Multi Play", 1, none_color)
    # screen.blit(multi_play, (260, 110))

    if 320 <= current_mouse_pos_x <= 435 and 165 <= current_mouse_pos_y <= 210:
        play_game = menu_font.render("start", 1, choose_color)
    else:
        play_game = menu_font.render("start", 1, none_color)
    screen.blit(play_game, (320, 165))

    if resume_game_botton:

        if 290 <= current_mouse_pos_x <= 470 and 100 <= current_mouse_pos_y <= 140:
            resume_game = menu_font.render("resume", 1, choose_color)
        else:
            resume_game = menu_font.render("resume", 1, none_color)
        screen.blit(resume_game, (290, 95))

    if 330 <= current_mouse_pos_x <= 435 and 345 <= current_mouse_pos_y <= 390:
        exit = menu_font.render("exit", 1, choose_color)
    else:
        exit = menu_font.render("exit", 1, none_color)
    screen.blit(exit, (330, 345))

    if resume_game_botton == True:
        if 270 <= current_mouse_pos_x <= 550 and 275 <= current_mouse_pos_y <= 310:
            save_game = save_and_quit_font.render("save and quit", 1, choose_color)
        else:
            save_game = save_and_quit_font.render("save and quit", 1, none_color)
        screen.blit(save_game, (270, 275))

def multi_player_menu():

    choose_color = (130, 200, 200)
    none_color = (160, 160, 160)

    pygame.draw.rect(screen, (0, 150, 150), (620, 70, 200, 400), 10)
    pygame.draw.rect(screen, (150, 150, 0), (600, 75, 190, 390), 5)
    data = requests.get("http://127.0.0.1:8000/api/blog/")
    data = data.json()

def write_to_database(object_to_write_1, object_2):
    database1 = open("database1", "wb")
    database2 = open("database2", "wb")

    object_to_write_1 = pickle.dumps(object_to_write_1)
    object_2 = pickle.dumps(object_2)

    database1.write(object_to_write_1)
    database2.write(object_2)
    database1.close()
    database2.close()


goal = []
start = []

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            pos2 = pygame.mouse.get_pos()
            current_mouse_pos_x = pos2[0]
            current_mouse_pos_y = pos2[1]
 #           print(x2)
  #          print(y2)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            x_click = pos[0]
            y_click = pos[1]

        if main_menu is False:

            for i in range(len(pieces)):

                if pieces[i].x == x and pieces[i].y == y and pieces[i].life and 0<=x<=7 and 0<=y<=7:
                   if pieces[i].color == "white" and turn[turn_index] is False:
                       start += x, y
                   if pieces[i].color == "black" and turn[turn_index] is True:
                       start += x, y
                if 0 <= x <= 7 and 0 <= y <= 7:
                    goal += x, y

                if len(start) > 1:

                    if turn[turn_index] is True and kish("black"):
                        b = kish_movement(start[-2], start[-1], "black")
                    elif turn[turn_index] is False and kish("white"):
                        b = kish_movement(start[-2], start[-1], "white")
                    else:
                        b = list_movement(start[-2], start[-1])
              #      print("b = ", b)
             #       print((goal[-2] * tile_size, goal[-1] * tile_size))

                    if (goal[-2] * tile_size, goal[-1] * tile_size) in b:
                         #   print("yes")
                        if move_permision(start[-2], start[-1], turn_index):
                            if not empty_tile(goal[-2], goal[-1]):
                                if turn[turn_index] is True and pieces[i].color == "black" and pieces[piece_index(goal[-2], goal[-1])].color == "white":
                                     pieces[piece_index(goal[-2], goal[-1])].life = False

                                if turn[turn_index] is False and pieces[i].color == "white" and pieces[piece_index(goal[-2], goal[-1])].color == "black":
                                     pieces[piece_index(goal[-2], goal[-1])].life = False

                            if turn[turn_index] is True and pieces[i].color == "black" and pieces[i].x == start[-2] and\
                                    pieces[i].y == start[-1]:
                                if pieces[i].rank == "k" and not kish_pos(goal[-2], goal[-1], "black") or pieces[i].rank != "k":

                                    move(start[-2], start[-1], goal[-2], goal[-1])

                                    turn_index += 1
                                    if turn_index > 1:
                                        turn_index = 0
                                    if kish("black") or kish("white"):
                                        kish_sound.play()

                            elif turn[turn_index] is False and pieces[i].color == "white" and pieces[i].x == start[-2]\
                                    and pieces[i].y == start[-1]:
                                if pieces[i].rank == "k" and not kish_pos(goal[-2], goal[-1], "white") or pieces[i].rank != "k":

                                    move(start[-2], start[-1], goal[-2], goal[-1])

                                    turn_index += 1
                                    if turn_index > 1:
                                        turn_index = 0
                                    if kish("black") or kish("white"):
                                        kish_sound.play()

    screen.fill((60, 70, 90))

    if maat_value is False:
        chess_board(width, height, tile_size, None)

    screen.blit(background, (1, 1))
    recognize_pices()

    if turn_index == 1:
        if kish("black"):
            pygame.draw.rect(screen, (255, 0, 0), (pieces[4].x * tile_size, pieces[4].y * tile_size, tile_size, tile_size), 5)
            maat_value = check_maat("black")

    if turn_index == 0:
        if kish("white"):
            pygame.draw.rect(screen, (255, 0, 0), (pieces[20].x * tile_size, pieces[20].y * tile_size, tile_size, tile_size), 5)
            maat_value = check_maat("white")

    if len(start) > 1:
        for i in range(len(pieces)):

            if turn[turn_index] is True and pieces[i].color == "black" and pieces[i].x == start[-2] and \
                    pieces[i].y == start[-1] or turn[turn_index] is False and pieces[i].color == "white" and \
                    pieces[i].x == start[-2] and pieces[i].y == start[-1]:
                if not kish("black") and not kish("white"):
                    show_movments(start[-2], start[-1])

                elif turn[turn_index] is True and kish("black"):
                    show_kish_movement(start[-2], start[-1], "black")
                elif turn[turn_index] is False and kish("white"):
                    show_kish_movement(start[-2], start[-1], "white")

            if pieces[i].life is False:
                moordeh_chin(i)
            if pieces[i].rank == "p" and 0 <= pieces[i].x <= 7:
                if pieces[i].color == "black" and pieces[i].y == 7 or pieces[i].color == "white" and pieces[i].y == 0:
#                    print(pieces[i].y)
                    choose_menu(pos[0], pos[1], current_mouse_pos_x, current_mouse_pos_y)

    if 700 <= current_mouse_pos_x <= 800 and 0 <= current_mouse_pos_y <= 50:
        pygame.draw.rect(screen, (150, 20, 80), (700, 0, 100, 50))
    else:
        pygame.draw.rect(screen, (200, 20, 20), (700, 0, 100, 50))   # رنگ دکمه مین منو

    if 700 <= x_click <= 800 and 0 <= y_click <= 50:
        main_menu = True
        resume_game_botton = True

    if main_menu:

        if 320 <= x_click <= 435 and 165 <= y_click <= 210:    #start
            maat_value = False
            main_menu = False
            turn_index = 0
            pieces = [piece(0, 0, "r", "black"), piece(1, 0, "h", "black"), piece(2, 0, "b", "black"),
                      piece(3, 0, "q", "black"), piece(4, 0, "k", "black"), piece(5, 0, "b", "black"),
                      piece(6, 0, "h", "black"), piece(7, 0, "r", "black"),
                      piece(0, 1, "p", "black"), piece(1, 1, "p", "black"), piece(2, 1, "p", "black"),
                      piece(3, 1, "p", "black"), piece(4, 1, "p", "black"), piece(5, 1, "p", "black"),
                      piece(6, 1, "p", "black"), piece(7, 1, "p", "black"),
                      piece(0, 7, "r", "white"), piece(1, 7, "h", "white"), piece(2, 7, "b", "white"),
                      piece(3, 7, "q", "white"), piece(4, 7, "k", "white"), piece(5, 7, "b", "white"),
                      piece(6, 7, "h", "white"), piece(7, 7, "r", "white"),
                      piece(0, 6, "p", "white"), piece(1, 6, "p", "white"), piece(2, 6, "p", "white"),
                      piece(3, 6, "p", "white"), piece(4, 6, "p", "white"), piece(5, 6, "p", "white"),
                      piece(6, 6, "p", "white"), piece(7, 6, "p", "white")]

        if 290 <= x_click <= 470 and 100 <= y_click <= 140:    #resume
            main_menu = False

        if 330 <= x_click <= 435 and 345 <= y_click <= 390:    #exit
            run = False
            if os.path.isfile("database1"):
                os.remove("database1")
            if os.path.isfile("database2"):
                os.remove("database2")

        if 335 <= x_click <= 440 and 275 <= y_click <= 310:    #save and quit
            write_to_database(pieces, turn_index)
            run = False
        # if 260 <= x_click <= 500 and 110 <= y_click <= 155:    #multi play
        #     multi_player_menu()

    if maat_value is True:
        if turn_index == 1:
            main_menu = True
            chess_board(width, height, tile_size, (255, 255, 255))     # white win
            white_win = end_game_font.render("white win!", 1, (150, 0, 0))
            screen.blit(white_win, (200, 300))
        elif turn_index == 0:
            main_menu = True
            chess_board(width, height, tile_size, (80, 80, 80))
            black_win = end_game_font.render("black win!", 1, (150, 0, 0))
            screen.blit(black_win, (200, 300))

    if main_menu:        # دکمه مین منو
        main_menu_()

    screen.blit(label, (705, 10))

    pygame.display.update()

    clock.tick(20)
pygame.quit()
