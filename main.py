import pygame
import cmath
from numpy import *

# The Images used in this project are Licensed under the Creative Commons Attribution-Share Alike 3.0 Unported


class Piece:
    def __init__(self, piece_type, team, location):
        self.type = piece_type
        self.team = team
        self.location = location
        self.possible_moves = {}
        self.possible_captures = {}
        self.turn_num = 0
        self.image = pygame.image.load("Black_Pawn.png")
        self.can_be_captured = False
        self.on_board = True
        if self.team:
            if self.type == "Pawn":
                self.image = pygame.image.load("Black_Pawn.png")
            elif self.type == "Bishop":
                self.image = pygame.image.load("Black_Bishop.png")
            elif self.type == "Castle":
                self.image = pygame.image.load("Black_Castle.png")
            elif self.type == "Knight":
                self.image = pygame.image.load("Black_Horse.png")
            elif self.type == "King":
                self.image = pygame.image.load("Black_King.png")
            elif self.type == "Queen":
                self.image = pygame.image.load("Black_Queen.png")
        else:
            if self.type == "Pawn":
                self.image = pygame.image.load("White_Pawn.png")
            elif self.type == "Bishop":
                self.image = pygame.image.load("White_Bishop.png")
            elif self.type == "Castle":
                self.image = pygame.image.load("White_Castle.png")
            elif self.type == "Knight":
                self.image = pygame.image.load("White_Horse.png")
            elif self.type == "King":
                self.image = pygame.image.load("White_King.png")
            elif self.type == "Queen":
                self.image = pygame.image.load("White_Queen.png")

    def castle(self, local_board):
        new_board = local_board
        checking = complex(1, 0)
        for i in range(4):
            j = 1
            while True:
                x = int(self.location[1]+checking.real*j)
                y = int(self.location[0]+checking.imag*j)
                if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                    if local_board[y][x] == "" or local_board[y][x] == "Filled":
                        self.possible_moves[str(self.location)] = [x, y]
                        new_board[y][x] = "Filled"
                    elif local_board[y][x].team != self.team:
                        self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                        local_board[y][x].can_be_captured = True
                        break
                    else:
                        break
                else:
                    break
                j += 1
            checking *= cmath.sqrt(-1)
        return new_board

    def knight(self, local_board):
        new_board = local_board
        checking = complex(2, 1)
        for i in range(4):
            x = int(self.location[1] + checking.real)
            y = int(self.location[0] + checking.imag)
            if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                if local_board[y][x] == "" or local_board[y][x] == "Filled":
                    self.possible_moves[str(self.location)] = [x, y]
                    new_board[y][x] = "Filled"
                elif local_board[y][x].team != self.team:
                    self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                    local_board[y][x].can_be_captured = True
            checking *= cmath.sqrt(-1)
        checking = complex(2, -1)
        for i in range(4):
            x = int(self.location[1] + checking.real)
            y = int(self.location[0] + checking.imag)
            if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                if local_board[y][x] == "" or local_board[y][x] == "Filled":
                    self.possible_moves[str(self.location)] = [x, y]
                    new_board[y][x] = "Filled"
                elif local_board[y][x].team != self.team:
                    self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                    local_board[y][x].can_be_captured = True
            checking *= cmath.sqrt(-1)
        return new_board

    def bishop(self, local_board):
        new_board = local_board
        checking = complex(1, 1)
        for i in range(4):
            j = 1
            while True:
                x = int(self.location[1] + checking.real * j)
                y = int(self.location[0] + checking.imag * j)
                if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                    if local_board[y][x] == "" or local_board[y][x] == "Filled":
                        self.possible_moves[str(self.location)] = [x, y]
                        new_board[y][x] = "Filled"
                    elif local_board[y][x].team != self.team:
                        self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                        local_board[y][x].can_be_captured = True
                        break
                    else:
                        break
                else:
                    break
                j += 1
            checking *= cmath.sqrt(-1)
        return new_board

    def queen(self, local_board):
        new_board = local_board
        checking = complex(1, 1)
        for i in range(4):
            j = 1
            while True:
                x = int(self.location[1] + checking.real * j)
                y = int(self.location[0] + checking.imag * j)
                if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                    if local_board[y][x] == "" or local_board[y][x] == "Filled":
                        self.possible_moves[str(self.location)] = [x, y]
                        new_board[y][x] = "Filled"
                    elif local_board[y][x].team != self.team:
                        self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                        local_board[y][x].can_be_captured = True
                        break
                    else:
                        break
                else:
                    break
                j += 1
            checking *= cmath.sqrt(-1)
        checking = complex(1, 0)
        for i in range(4):
            j = 1
            while True:
                x = int(self.location[1] + checking.real * j)
                y = int(self.location[0] + checking.imag * j)
                if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                    if local_board[y][x] == "" or local_board[y][x] == "Filled":
                        self.possible_moves[str(self.location)] = [x, y]
                        new_board[y][x] = "Filled"
                    elif local_board[y][x].team != self.team:
                        self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                        local_board[y][x].can_be_captured = True
                        break
                    else:
                        break
                else:
                    break
                j += 1
            checking *= cmath.sqrt(-1)
        return new_board

    def king(self, local_board):
        new_board = local_board
        checking = complex(1, 0)
        for i in range(4):
            x = int(self.location[1] + checking.real)
            y = int(self.location[0] + checking.imag)
            if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                if local_board[y][x] == "" or local_board[y][x] == "Filled":
                    self.possible_moves[str(self.location)] = [x, y]
                    new_board[y][x] = "Filled"
                elif local_board[y][x].team != self.team:
                    self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                    local_board[y][x].can_be_captured = True
            checking *= cmath.sqrt(-1)
        checking = complex(1, 1)
        for i in range(4):
            x = int(self.location[1] + checking.real)
            y = int(self.location[0] + checking.imag)
            if not x < 0 and not x > len(local_board[0]) - 1 and not y < 0 and not y > len(local_board) - 1:
                if local_board[y][x] == "" or local_board[y][x] == "Filled":
                    self.possible_moves[str(self.location)] = [x, y]
                    new_board[y][x] = "Filled"
                elif local_board[y][x].team != self.team:
                    self.possible_captures[str([x, y])] = [local_board[y][x].type, local_board[y][x].team]
                    local_board[y][x].can_be_captured = True
            checking *= cmath.sqrt(-1)
        return new_board

    def pawn(self, local_board):
        new_board = local_board
        if self.team:
            if local_board[self.location[0] + 1][self.location[1]] == "":
                self.possible_moves[str(self.location)] = [self.location[0]+1, self.location[1]]
                new_board[self.location[0]+1][self.location[1]] = "Filled"
                if self.turn_num == 0:
                    self.possible_moves[str(self.location)] = [self.location[0] + 2, self.location[1]]
                    new_board[self.location[0] + 2][self.location[1]] = "Filled"
            if 0 < self.location[0]+1 < len(local_board) and 0 < self.location[1]+1 < len(local_board[0]):
                if local_board[self.location[0] + 1][self.location[1] + 1] != "" and \
                        local_board[self.location[0] + 1][self.location[1] + 1] != "Filled":
                    if local_board[self.location[0] + 1][self.location[1] + 1].team != self.team:
                        local_board[self.location[0] + 1][self.location[1] + 1].can_be_captured = True
                if local_board[self.location[0] + 1][self.location[1] - 1] != "" and \
                        local_board[self.location[0] + 1][self.location[1] - 1] != "Filled":
                    if local_board[self.location[0] + 1][self.location[1] - 1].team != self.team:
                        local_board[self.location[0] + 1][self.location[1] - 1].can_be_captured = True
        else:
            if local_board[self.location[0] - 1][self.location[1]] == "":
                self.possible_moves[str(self.location)] = [self.location[0]-1, self.location[1]]
                new_board[self.location[0]-1][self.location[1]] = "Filled"
                if self.turn_num == 0:
                    self.possible_moves[str(self.location)] = [self.location[0] - 2, self.location[1]]
                    new_board[self.location[0] - 2][self.location[1]] = "Filled"
            if 0 < self.location[0] + 1 < len(local_board) and 0 < self.location[1] + 1 < len(local_board[0]):
                if local_board[self.location[0] - 1][self.location[1] + 1] != "" and \
                        local_board[self.location[0] - 1][self.location[1] + 1] != "Filled":
                    if local_board[self.location[0] - 1][self.location[1] + 1].team != self.team:
                        local_board[self.location[0] - 1][self.location[1] + 1].can_be_captured = True
                if local_board[self.location[0] - 1][self.location[1] - 1] != "" and \
                        local_board[self.location[0] - 1][self.location[1] - 1] != "Filled":
                    if local_board[self.location[0] - 1][self.location[1] - 1].team != self.team:
                        local_board[self.location[0] - 1][self.location[1] - 1].can_be_captured = True
        return new_board

    def gen_possible_moves(self, board):
        self.possible_captures = {}
        self.possible_moves = {}
        moves = {
            "Castle": self.castle,
            "Knight": self.knight,
            "Bishop": self.bishop,
            "Queen": self.queen,
            "King": self.king,
            "Pawn": self.pawn
        }
        moves[self.type](board)

    def gen_display_possible_moves(self, board, turn):
        self.possible_captures = {}
        self.possible_moves = {}
        now_turn = turn % 2
        moves = {
            "Castle": self.castle,
            "Knight": self.knight,
            "Bishop": self.bishop,
            "Queen": self.queen,
            "King": self.king,
            "Pawn": self.pawn
        }
        if now_turn == 0 and not self.team:
            board = moves[self.type](board)
        elif now_turn == 1 and self.team:
            board = moves[self.type](board)
        return board


def chess_check_check():
    result = False
    # local_board = board
    # for i in range(len(local_board)):
    #     for j in range(len(local_board[0])):
    #         local_board[i][j] = board[i][j]
    # result = False
    # for i in range(len(local_board)):
    #     for j in range(len(local_board[0])):
    #         if local_board[i][j] != "" and local_board[i][j] != "Filled":
    #             local_board[i][j].gen_display_possible_moves(local_board, turn)
    # for i in range(len(local_board)):
    #     for j in range(len(local_board[0])):
    #         if local_board[i][j] != "" and local_board[i][j] != "Filled":
    #             if local_board[i][j].can_be_captured:
    #                 if local_board[i][j].type == "King":
    #                     result = True
    # for i in range(8):
    #     for j in range(8):
    #         if local_board[i][j] == "Filled":
    #             local_board[i][j] = ""
    #         elif local_board[i][j] != "":
    #             local_board[i][j].can_be_captured = False
    return result


def chess_checkmate_check(board):
    print(board)


def make_board(board):
    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[i])):
            piece_type = i < 4
            cur_piece = ""
            if board[i][j] != "":
                cur_piece = Piece(board[i][j], piece_type, [i, j])
            new_board[i].append(cur_piece)

    return new_board


def main():
    # Initialising the pygame window
    window_height = 504
    window_width = 504
    block_size = window_height/8
    pygame.init()
    pygame.display.set_caption("Chess")
    screen = pygame.display.set_mode((window_width, window_height))
    initial_board = [
        ["Castle", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Castle"],
        ["Pawn",   "Pawn",   "Pawn",   "Pawn",  "Pawn", "Pawn",   "Pawn",   "Pawn"],
        ["",       "",       "",       "",      "",     "",       "",       ""],
        ["",       "",       "",       "",      "",     "",       "",       ""],
        ["",       "",       "",       "",      "",     "",       "",       ""],
        ["",       "",       "",       "",      "",     "",       "",       ""],
        ["Pawn",   "Pawn",   "Pawn",   "Pawn",  "Pawn", "Pawn",   "Pawn",   "Pawn"],
        ["Castle", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Castle"],
             ]
    board = make_board(initial_board)
    mouse_down = False
    position_selected = None
    last_selected = None
    turn = 0
    prev_turn = turn
    game = True
    check = False
    while True:
        while game:
            if prev_turn != turn:
                print(turn)
            prev_turn = turn
            screen.fill((108, 156, 81))
            pygame.draw.rect(screen, (245, 245, 237), pygame.Rect(0, window_height/2, window_width, window_height/2))
            if turn % 2 == 0:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(block_size*8, window_height / 2,
                                                                block_size, block_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(block_size * 8, window_height / 2 - block_size,
                                                                block_size, block_size))
            # Gets the mouse position every frame
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                # Quits the code if the cross on the game window if pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Gets whether the mouse is pressed and changes a variable to store it
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_down:
                        mouse_down = False
                        position_selected = [int(mouse_pos[0] / block_size), int(mouse_pos[1] / block_size)]
                        if position_selected[0] < 8:
                            if board[position_selected[1]][position_selected[0]] == "Filled":
                                prev_turn = turn
                                turn += 1
                                board[last_selected[1]][last_selected[0]].location = [position_selected[1],
                                                                                      position_selected[0]]
                                board[last_selected[1]][last_selected[0]].turn_num += 1
                                board[position_selected[1]][position_selected[0]] = \
                                    board[last_selected[1]][last_selected[0]]
                                board[last_selected[1]][last_selected[0]] = ""
                                if check:
                                    print("Game Over")
                            elif board[position_selected[1]][position_selected[0]] != "":
                                if board[position_selected[1]][position_selected[0]].can_be_captured:
                                    prev_turn = turn
                                    turn += 1
                                    board[last_selected[1]][last_selected[0]].location = [position_selected[1],
                                                                                          position_selected[0]]
                                    board[last_selected[1]][last_selected[0]].turn_num += 1
                                    board[position_selected[1]][position_selected[0]] = \
                                        board[last_selected[1]][last_selected[0]]
                                    board[last_selected[1]][last_selected[0]] = ""
                                    print("captured")
                                    if check:
                                        print("Game Over")
                                else:
                                    for i in range(8):
                                        for j in range(8):
                                            if board[i][j] == "Filled":
                                                board[i][j] = ""
                                            elif board[i][j] != "":
                                                board[i][j].can_be_captured = False
                                    mouse_down = True

                    else:
                        mouse_down = True
                        position_selected = [int(mouse_pos[0] / block_size), int(mouse_pos[1] / block_size)]

            if mouse_down:
                last_selected = [position_selected[0], position_selected[1]]
                if last_selected[0] < 8:
                    if board[position_selected[1]][position_selected[0]] != "" and \
                            board[position_selected[1]][position_selected[0]] != "Filled":
                        board = \
                            board[position_selected[1]][position_selected[0]].gen_display_possible_moves(board, turn)
            else:
                for i in range(8):
                    for j in range(8):
                        if board[i][j] == "Filled":
                            board[i][j] = ""
                        elif board[i][j] != "":
                            board[i][j].can_be_captured = False

            for i in range(8):
                for j in range(8):
                    rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
                    if i % 2 == 1:
                        if j % 2 == 1:
                            pygame.draw.rect(screen, (245, 255, 237), rect)
                        elif j % 2 == 0:
                            pygame.draw.rect(screen, (108, 166, 81), rect)
                    elif i % 2 == 0:
                        if j % 2 == 1:
                            pygame.draw.rect(screen, (108, 166, 81), rect)
                        elif j % 2 == 0:
                            pygame.draw.rect(screen, (245, 255, 237), rect)
                    if board[i][j] == "Filled":
                        pygame.draw.circle(screen, (186, 186, 186),
                                           (j * block_size+block_size/2, i * block_size+block_size/2), 10)
                    if board[i][j] != "Filled" and board[i][j] != "":
                        if board[i][j].can_be_captured:
                            pygame.draw.circle(screen, (186, 186, 186),
                                               (j * block_size + block_size / 2, i * block_size + block_size / 2), 30)
                        if board[i][j].on_board:
                            screen.blit(board[i][j].image, rect)

            # Updates the display window
            pygame.display.update()


if __name__ == '__main__':
    main()
