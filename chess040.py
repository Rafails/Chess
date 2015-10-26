__author__ = 'Goldsmitd'

import tkinter as tk
from tkinter import ttk
import tkinter.font as font



class Condition:

    def range(x,y):
        return x > 8 and y > 8

    def if_figure(board,x,y):
        return board[x][y].sl == '  '

    def same_team(x1,y1,x2,y2,board):
        if board[x1][y1].team == board[x2][y2].team:
            return True
        else:
            return False


    def kill(x1,y1,x2,y2,board):
        if board[x1][y1].team == 'white' and board[x2][y2].team == 'black':
            return True
        elif board[x1][y1].team == 'black' and board[x2][y2].team == 'white':
            return True
        else:
            return False

    def Pawnkill(x1,y1,x2,y2,board):
        if board[x1][y1].team == 'white' and board[x2][y2].team == 'black' and board[x1][y1].name == 'Pawn':
            return True
        elif board[x1][y1].team == 'black' and board[x2][y2].team == 'white'and board[x1][y1].name == 'Pawn':
            return True
        else:
            return False


    def solid(x1,y1,x2,y2,board):
        if board[x1][y1].name=='Rook':
            if x2>x1:
                for i in range(x1+1,x2):
                    if board[i][y1].sl != '  ':
                        return False
                        break
            elif x2<x1:
                for i in range(x2+1,x1):
                    if board[i][y1].sl != '  ':
                        return False
                        break
            elif y2>y1:
                for j in range(y1+1,y2):
                    if board[x1][j].sl != '  ':
                        return False
                        break
            elif y2<y1:
                for j in range(y2+1,y1):
                    if board[x1][j].sl != '  ':
                        return False
                        break
            else:
                return True


        elif board[x1][y1].name=='Bishop':
            if x2>x1 and y2>y1:
                for i in range(x1+1,x2):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2<x1 and y2<y1:
                for i in range(x2+1,x1):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2<x1 and y2>y1:
                for i in range(x2+1,x1):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2>x1 and y2<y1:
                for i in range(x1+1,x2):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '  ':
                            return False
                            break
            else:
                return True

        elif board[x1][y1].name=='Queen':
            if x2>x1 and y2>y1:
                for i in range(x1+1,x2):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2<x1 and y2<y1:
                for i in range(x2+1,x1):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2<x1 and y2>y1:
                for i in range(x2+1,x1):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2>x1 and y2<y1:
                for i in range(x1+1,x2):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '  ':
                            return False
                            break
            elif x2>x1:
                for i in range(x1+1,x2):
                    if board[i][y1].sl != '  ':
                        return False
                        break
            elif x2<x1:
                for i in range(x2+1,x1):
                    if board[i][y1].sl != '  ':
                        return False
                        break
            elif y2>y1:
                for j in range(y1+1,y2):
                    if board[x1][j].sl != '  ':
                        return False
                        break
            elif y2<y1:
                for j in range(y2+1,y1):
                    if board[x1][j].sl != '  ':
                        return False
                        break

            else:
                return True



        else:
            return True


class Number:
    def __init__(self,uni):
        self.sl='XX'
        self.uni=uni



class Empty:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Empty'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni


class Rook:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Rook'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni

    def req(self,sx,sy,dx,dy,board):
            if  ( dx==sx or dy==sy ) :
                return True
            else:
                return False


class Knight:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Knight'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni


    def req(self,sx,sy,dx,dy,board):
            if  (abs(dx - sx)**2+abs(dy - sy)**2 == 5) :
                return True
            else:
                return False


class Bishop:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Bishop'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni


    def req(self,sx,sy,dx,dy,board):
            if  (abs(dx - sx)==abs(dy - sy)) :
                return True
            else:
                return False


class Queen:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Queen'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni

    def req(self,sx,sy,dx,dy,board):
            if  (dx == sx or dy == sy or (abs(dx - sx) == abs(dy - sy))) :
                return True
            else:
                return False


class King:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'King'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni

    def req(self,sx,sy,dx,dy,board):
            if  abs(dx-sx) < 2 and abs(dy-sy) <  2 :
                return True
            else:
                return False


class Pawn:
    def __init__(self,x,y,sl,team,uni):
        self.name = 'Pawn'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
        self.uni = uni


    def req(self,sx,sy,dx,dy,board):
            if board[sx][sy].team == "white" and dx-sx == -1:
                return True
            elif board[sx][sy].team == 'black' and dx-sx == 1:
                return True
            else:
                return False


class ChessBoard:
    def __init__(self):
        self.board = [[Empty(x='',y='',sl='  ',team='',uni='')]*9 for _ in range(9)]
        self.board[0][0] = Rook(x=0,y=0,sl='r',team='black', uni=u'\u265c')
        self.board[0][1] = Knight(x=0,y=1,sl='n',team='black', uni=u'\u265e')
        self.board[0][2] = Bishop(x=0,y=2,sl='b',team='black', uni=u'\u265d')
        self.board[0][3] = Queen(x=0,y=3,sl='q',team='black', uni=u'\u265b')
        self.board[0][4] = King(x=0,y=4,sl='k',team='black', uni=u'\u265a')
        self.board[0][5] = Bishop(x=0,y=5,sl='b',team='black', uni=u'\u265d')
        self.board[0][6] = Knight(x=0,y=6,sl='n',team='black', uni=u'\u265e')
        self.board[0][7] = Rook(x=0,y=7,sl='r',team='black', uni=u'\u265c')
        self.board[1][0] = Pawn(x=1,y=0,sl='p',team='black', uni=u'\u265f')
        self.board[1][1] = Pawn(x=1,y=1,sl='p',team='black', uni=u'\u265f')
        self.board[1][2] = Pawn(x=1,y=2,sl='p',team='black', uni=u'\u265f')
        self.board[1][3] = Pawn(x=1,y=3,sl='p',team='black', uni=u'\u265f')
        self.board[1][4] = Pawn(x=1,y=4,sl='p',team='black', uni=u'\u265f')
        self.board[1][5] = Pawn(x=1,y=5,sl='p',team='black', uni=u'\u265f')
        self.board[1][6] = Pawn(x=1,y=6,sl='p',team='black', uni=u'\u265f')
        self.board[1][7] = Pawn(x=1,y=7,sl='p',team='black', uni=u'\u265f')
        self.board[7][0] = Rook(x=7,y=0,sl='R',team='white', uni=u'\u2656')
        self.board[7][1] = Knight(x=7,y=1,sl='N',team='white', uni=u'\u2658')
        self.board[7][2] = Bishop(x=7,y=2,sl='B',team='white', uni=u'\u2657')
        self.board[7][3] = Queen(x=7,y=3,sl='Q',team='white', uni=u'\u2655')
        self.board[7][4] = King(x=7,y=4,sl='K',team='white', uni=u'\u2654')
        self.board[7][5] = Bishop(x=7,y=5,sl='B',team='white', uni=u'\u2657')
        self.board[7][6] = Knight(x=7,y=6,sl='N',team='white', uni=u'\u2658')
        self.board[7][7] = Rook(x=7,y=7,sl='R',team='white', uni=u'\u2656')
        self.board[6][0] = Pawn(x=6,y=0,sl='P',team='white', uni=u'\u2659')
        self.board[6][1] = Pawn(x=6,y=1,sl='P',team='white', uni=u'\u2659')
        self.board[6][2] = Pawn(x=6,y=2,sl='P',team='white', uni=u'\u2659')
        self.board[6][3] = Pawn(x=6,y=3,sl='P',team='white', uni=u'\u2659')
        self.board[6][4] = Pawn(x=6,y=4,sl='P',team='white', uni=u'\u2659')
        self.board[6][5] = Pawn(x=6,y=5,sl='P',team='white', uni=u'\u2659')
        self.board[6][6] = Pawn(x=6,y=6,sl='P',team='white', uni=u'\u2659')
        self.board[6][7] = Pawn(x=6,y=7,sl='P',team='white', uni=u'\u2659')
        for i in range(9):
            self.board[i][8 ]= Number(uni=str(i))
        for j in range(9):
            self.board[8][j] = Number(uni=str(j))

    def display(self):
        for i in range(9):
            for j in range(9):
                print (self.board[i][j].sl, end=' ')
            print()



    def move(self,sx,sy,dx,dy):
        mark_same=Condition.same_team(sx,sy,dx,dy,self.board)
        mark_kill=Condition.kill(sx,sy,dx,dy,self.board)
        mark_Pawnkill=Condition.Pawnkill(sx,sy,dx,dy,self.board)
        mark_solid=Condition.solid(sx,sy,dx,dy,self.board)
        mark_move=self.board[sx][sy].req(sx,sy,dx,dy,self.board)
        if mark_solid==False:
            myapp.sLB['text']='Figures are not ghosts'

        elif (mark_Pawnkill == True and abs(dx-sx) == abs(dy-sy) and mark_same == False):
            self.board[dx][dy] = self.board[sx][sy]
            self.board[dx][dy].x = dx
            self.board[dx][dy].y = dy
            self.board[sx][sy] = Empty(x='',y='',sl='  ',team='',uni='')
            return self.board


        elif (mark_move == True and mark_Pawnkill == False and (mark_kill == True or mark_same == False)):
            self.board[dx][dy] = self.board[sx][sy]
            self.board[dx][dy].x = dx
            self.board[dx][dy].y = dy
            self.board[sx][sy] = Empty(x='',y='',sl='  ',team='',uni='')
            return self.board

        else:
             myapp.sLB['text'] = 'Figure can not move here, try again'



class MyApp:
    def __init__(self,parent):
        self.tupleY = None
        self.parent = parent
        self.myContainer = tk.Frame(self.parent)
        self.myContainer.pack()
        self.cb = ChessBoard()
        #right frame
        self.rightframe = tk.Frame(self.myContainer, bg='white', width=150, height=150, relief='groove')
        self.rightframe.pack(side='top')
        #output frame
        self.outputFrame = tk.Frame(self.myContainer, bg='white', width=150, height=150, relief='groove')
        self.outputFrame.pack(side='bottom')
        self.display_app()
        #state label
        self.sLB = tk.Label(self.outputFrame,text='dupa', bg='lightgrey')
        self.sLB.grid(row=7, column=1)




    def display_app(self):
        self.names = [[0 for x in range(9)] for x in range(9)]
        for i in range(9):
            for j in range(9):
                tupleIJ = (i,j)
                self.names[i][j] = tk.Button(self.rightframe, background='red', width=6, height=3, relief='flat', font=('Arial Unicode MS',12),
                                             command=lambda tupleIJ=tupleIJ :self.click(tupleIJ), text=self.cb.board[i][j].uni)
                if (((i%2==1 and j%2==0) or (i%2==0 and j%2==1)) and i<8 and j<8):
                    self.names[i][j].config(background = 'darkgrey')
                elif i==8 or j==8:
                    self.names[i][j].config(background = 'black')
                    self.names[i][j].config(foreground = 'white')
                else:
                    self.names[i][j].config(background='white')
                self.names[i][j].grid(row=i, column=j)


    def click(self, tupleIJ):
        if self.names[tupleIJ[0]][tupleIJ[1]]['bg'] == 'yellow':
            #returning previous color of square
            for i in range(9):
                for j in range(9):
                    if (((i%2==1 and j%2==0) or (i%2==0 and j%2==1)) and i<8 and j<8):
                        self.names[i][j]['bg'] = 'darkgrey'
                    elif i==8 or j==8:
                        self.names[i][j]['bg'] = 'black'
                        self.names[i][j]['foreground'] = 'white'
                    else:
                        self.names[i][j]['bg'] = 'white'
                    self.names[i][j].grid(row=i, column=j)
                self.tupleY = None
            #moving
        elif self.tupleY is not None:
            self.names[tupleIJ[0]][tupleIJ[1]]['bg'] = 'red'
            self.tupleR = (tupleIJ[0],tupleIJ[1])
            sx = self.tupleY[0]
            sy = self.tupleY[1]
            dx = self.tupleR[0]
            dy = self.tupleR[1]
            self.cb.move(sx, sy, dx, dy)
            self.tupleY = None
            self.tupleY = None
            self.display_app()


        else:
            #change color of square on yellow
            self.names[tupleIJ[0]][tupleIJ[1]]['bg'] = 'yellow'
            self.tupleY = (tupleIJ[0],tupleIJ[1])
            return self.tupleY





root = tk.Tk()
myapp=MyApp(root)
root.mainloop()
