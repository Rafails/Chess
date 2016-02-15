import sys
import os
clear = "\n" * 100
#ZROBIONE PIONKI ZE MGOA SIE RUSZAC O DWA DO PRZODU JAK JEST POCZATEK ICH RUCHU I ZABIJAC xDD QUICK FIX ZROBIONY
#TERAZ ROBIOENIE ZAMIANY PIONKOW NA TO CO SIE CHCE



class Game:
    """
    This is a main part of this program. There are set main methods which are responsible for conducting a chess game
    """
    def __init__(self):

        # args2plater1 = self.player_args('1')
        # args2player2 = self.player_args('2')
        # self.Player1 = Player(name=args2plater1[0], team=args2plater1[1], character=args2plater1[2])
        # self.Player2 = Player(name=args2player2[0], team=args2player2[1], character=args2player2[2])
        self.Player1 = Player('j', 'black', 'human')
        self.Player2 = Player('k', 'white', 'human')
        self.cboard = Chessboard()
        self.limitwins = 2
        self.limimitrounds = 5
        self.currentround = len(self.cboard.historymove)+1
        self.game_run()

    def game_run(self):
        #print(self.currentround)
        for i in range(99):
            self.cboard.display_board()
            self.make_move()
        # self.cboard.display_board()
        # self.undo_move()
        # self.cboard.display_board()
        #print(clear)

    def check_player_team(self, sx, sy, player):
        if self.cboard.board[sx][sy].team == player.team:
            return True
        else:
            return False

    def current_color_team(self):
        if len(self.cboard.historymove) % 2 == 0:
            return 'white'
        else:
            return 'black'

    def check_win(self):
        return False


    def player_args(self, playerno):
        print('please give a name of player %s' % playerno )
        name = str(input())
        print('please give a team  of player %s' % playerno )
        team = str(input())
        print('please give a character of player %s' % playerno )
        character = str(input())
        return name, team, character





       #methods responsible for making or undoing a move
    #-------------------------------------------------------------------
    def make_move(self):
        # checking a equality of color of piece and color of player
        while True:
            print('give start coordinates')
            sx = int(input())
            sy = int(input())
            print(self.cboard.board[sx][sy].team)
            print(self.current_color_team())
            if self.cboard.board[sx][sy].team == self.current_color_team():
                break
            else:
                print('wrong color')
                continue
        print('give destination coordinates')
        dx = int(input())
        dy = int(input())


        #checking a possibility of killing by pawn
        if self.cboard.board[sx][sy].symbol == 'P' and self.cboard.if_move_kill_pawn(sx, sy, dx, dy) == True:
            self.cboard.board[sx][sy], self.cboard.board[dx][dy] = self.cboard.board[dx][dy], self.cboard.board[sx][sy]
            self.cboard.historymove.append([sx, sy, dx, dy, self.cboard.board[sx][sy], self.cboard.board[dx][dy]])

            #checking a possibility of changing a pawn to other piece
            self.cboard.change_pawn_2_piece(dx, dy)
        else:
            print('pawn can not kill this figure')

            # checking a condition on move for specific piece
            if self.cboard.symbol2check[self.cboard.board[sx][sy].symbol](sx, sy, dx, dy) == True:

                # checking condition of free way
                if self.cboard.check_free_way(sx, sy, dx, dy) == True:

                    #checking a possibility of killing a enemy figure or possibility of moving on empty field
                    if self.cboard.if_kill(sx, sy, dx, dy) == True or self.cboard.if_kill(sx, sy, dx, dy) == None:
                        self.cboard.board[sx][sy], self.cboard.board[dx][dy] = self.cboard.board[dx][dy], self.cboard.board[sx][sy]
                        self.cboard.historymove.append([sx, sy, dx, dy, self.cboard.board[sx][sy], self.cboard.board[dx][dy]])

                        #checking a possibility of changing a pawn to other piece
                        self.cboard.change_pawn_2_piece(dx, dy)
                    else:
                        print('You cant kill your own figure')

                else:
                    print('Piece is not like a ghost')

            else:
                print('This is not movement for this piece')




    def undo_move(self):
        print('do you want to remove your choice? y/n')
        answer = str(input())
        if answer == 'y':
            end = len(self.cboard.historymove)-1
            self.cboard.board[self.cboard.historymove[end][2]][self.cboard.historymove[end][3]], self.cboard.board[self.cboard.historymove[end][0]][self.cboard.historymove[end][1]] \
            = self.cboard.board[self.cboard.historymove[end][0]][self.cboard.historymove[end][1]], self.cboard.board[self.cboard.historymove[end][2]][self.cboard.historymove[end][3]]
            self.cboard.historymove.pop()
    #--------------------------------------------------------------------------------------------------






class Player:
    """
    This class is a Player-class. It holds 6 fields: name, team , wins, losses, score, and character.
    First fifth attributes are easy to explain so It is no necessary to describe it.
    The sixth attribute - character marks a nature of player - a human or AI.
    """
    def __init__(self, name, team, character):
        self.name = name
        self.team = team
        self.wins = 0
        self.losses = 0
        self.score = self.wins - self.losses
        self.character = character


class Square:
    """
    This class represent a one field on a chessbord. It has got 4 attributes: x , y, symbol and team.
    Axis x and y have reverse orientation otherwise than classic coordinate system.
    """
    def __init__(self, x, y, symbol, team):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.team = team


class Chessboard:
    """
    Chessboard class represent a real chessboard. It is split on 64 fields. This class holds methods,
    which were responsible for checking a possibility of make a move by piece
    """
    def __init__(self):
        self.board = [[0 for x in range(8)] for x in range(8)]
        for i in range(8):
            for j in range(8):
                self.board[i][j] = (Square(x=i, y=j, symbol=self.symbol_set(i,j), team=self.team_set(i,j)))
        self.symbol2check = {
            'P': self.check_pawn,
            'R': self.check_rook,
            'N': self.check_knight,
            'B': self.check_bishop,
            'Q': self.check_queen,
            'K': self.check_king
        }

        self.board[1][1] = Square(1,1,'R','black')

        self.board[1][0] = Square(1,0,'P','white')

        self.historymove = []

    # methods which are responsible for setting pieces on chessboard
    #--------------------------------------------------------------------------
    def symbol_set(self, x, y):
        if x == 1 or  x == 6:
            return 'P'
        elif (x == 0 or x == 7) and (y == 0 or y == 7):
            return 'R'
        elif (x == 0 or x == 7) and (y == 1 or y == 6):
            return 'N'
        elif (x == 0 or x == 7) and (y == 2 or y == 5):
            return 'B'
        elif (x == 0 or x == 7) and (y == 3):
            return 'Q'
        elif (x == 0 or x == 7) and (y == 4):
            return 'K'
        else:
            return 'E'

    def team_set(self, x, y):
        if x == 0 or x == 1:
            return 'black'
        elif x == 6 or x ==  7:
            return 'white'
        else:
            return None
    #----------------------------------------------------------------------------

    # this method display a chessboard on screen
    #----------------------------------------------
    def display_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j].symbol, end=' ')
            print()

    def if_square_empty(self, x, y):
        if self.board[x][y].symbol == 'E':
            return True
        else:
            return False
    #-------------------------------------------------

    def change_pawn_2_piece(self, x2, y2):

        if ((self.board[0][y2].team == 'white' and self.board[0][y2].symbol == 'P') or
            (self.board[0][y2].team == 'black' and self.board[7][y2].symbol == 'P')):
            print(' Please give a symbol of piece which you want to have : R, N, B, Q')
            choice = str(input())
            self.board[x2][y2].symbol = choice
    # Conditions for specific piece move or kill
    #--------------------------------------------------------------
    def if_move_kill_pawn(self, x1, y1, x2, y2):
        if self.board[x1][y1].team == 'white' and self.board[x2][y2].team == 'black':
            if x1 - x2 == 1 and abs(y1 - y2) == 1:
                return True
            else:
                return False
        elif self.board[x1][y1].team == 'black' and self.board[x2][y2].team == 'white':
            if x1 - x2 == -1 and abs(y1 - y2) == 1:
                return True
            else:
                return False
        else:
            return False



    def if_kill(self, x1, y1, x2, y2):
        if self.board[x1][y1].symbol == 'P':
            return 'Pawn cant kill foward'

        elif self.board[x1][y1].team == self.board[x2][y2].team:
            print('It is not possible to kill your own figure')
            return False
        elif self.board[x2][y2].symbol == 'E':
            print('It was empty field here ')
            return None
        else:
            print('FINISH HIM')
            return True


    def  check_pawn(self, x1, y1, x2, y2):
        if self.board[x1][y1].team == 'black' and x1 == 1 and abs(x1-x2) < 3 and y1 == y2:
            return True
        elif self.board[x1][y1].team == 'white' and x1 == 6 and abs(x1-x2) < 3 and y1 == y2:
            return True
        elif abs(x1-x2) == 1 and y1 == y2:
            return True
        else:
            return False

    def  kill_pawn(self, x1, y1, x2, y2):
        if abs(x1-x2) == 1 and  abs(y1-y2) == 1:
            return True
        else:
            return False

    def check_rook(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            return True
        else:
            False

    def  check_knight(self, x1, y1, x2, y2):
        if abs(abs(x1-x2) + abs(y1-y2)) == 1:
            return True
        else:
            return False

    def  check_bishop(self, x1, y1, x2, y2):
        if abs(x1-x2) == abs(y1-y2):
            return True
        else:
            return False

    def check_queen(self, x1, y1, x2, y2):
        if (self.check_bishop(x1, y1, x2, y2) == True or
                    self.check_rook(x1, y1, x2, y2) == True):
            return True
        else:
            return False

    def check_king(self, x1, y1, x2, y2):
        if abs(x1 - x2) < 2 or abs(y1 - y2) < 2:
            return True
        else:
            return False
    #------------------------------------------------------------------

    # Condition on free way

    def check_free_way(self, x1, y1, x2, y2):

        #if  difference is equal 1
        if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
            return True

        if self.board[x1][y1].symbol == 'P':
            if self.board[x1][y1].team == 'white' and self.board[x1-1][y1].symbol == 'E':
                return True
            elif self.board[x1][y1].team == 'black' and self.board[x1+1][y1].symbol == 'E':
                return True
            else:
                return False




        if self.board[x1][y1].symbol == 'R' or self.board[x1][y1].symbol == 'Q':
            if x1 == x2:
                for i in range(abs(y1-y2)):
                    if y1 > y2:
                        if not self.board[x1][y1-i] == 'E':
                            return False
                        else:
                            return True
                    elif y1 < y2:
                        if not self.board[x1][y1+i] == 'E':
                            return False
                        else:
                            return True
            elif y1 == y2:
                    for i in range(abs(y1-y2)):
                        if x1 > x2:
                            if not self.board[x1-i][y1] == 'E':
                                return False
                            else:
                                return True
                        elif x1 < x2:
                            if not self.board[x1+i][y1] == 'E':
                                return False
                            else:
                                return True



        if self.board[x1][y1].symbol == 'B' or self.board[x1][y1].symbol == 'Q':
            for i in range(abs(x1 - x2)):
                if x1 > x2 and y1 > y2:
                    if not self.board[x1-i][y1-i].symbol == 'E':
                        return False
                    else:
                        return True

                if x1 > x2 and y1 < y2:
                    if not self.board[x1-i][y1+i].symbol == 'E':
                        return False
                    else:
                        return True

                if x1 < x2 and y1 > y2:
                    if not self.board[x1+i][y1-i].symbol == 'E':
                        return False
                    else:
                        return True

                if x1 < x2 and y1 < y2:
                    if not self.board[x1+i][y1+i].symbol == 'E':
                        return False
                    else:
                        return True

help(Game)
Game()
# g.game_run()
help(Player)