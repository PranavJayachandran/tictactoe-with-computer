from tkinter import *
from tkinter import messagebox


def player(a,ch,x,y):
    if a[x][y]=="_":
        a[x][y]=ch
        b[x][y].configure(text="X")
    else :
        print("Cannot put value there")
        return 0
    return 1

def cancontinue(a):
   for x in a:
       for y in x:
           if y=="_":
               return 1 
   return 0

def iswinner(a,move):
    for i in range(0,3):
        done=1
        for j in range(0,3):
            if a[i][j]!=move:
                done=0
        if done==1:
            return done
    for j in range(0,3):
        done=1
        for i in range(0,3):
            if a[i][j]!=move:
                done=0
        if done==1:
            return done
    done=1
    for i in range(0,3):
        if a[i][i]!=move:
            done=0
    if done==1:
        return done
    if a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[0][2]==move:
        return 1
    return 0

def getBestMove(a,move,compmove):
    choose=lambda move:"X" if move=="O" else "O"
    value,x,y=0,0,0
    temp=0  
    if(cancontinue(a)==0):
        return 0
    if(iswinner(a,choose(move))==1 and move == compmove):
        return -1
    elif(iswinner(a,choose(move))==1 and move == choose(compmove)):
        temp=1
    
    
    for i in range (0,3):
        for j in range(0,3):

            if a[i][j]=="_":
                x=a
                x[i][j]=move
                temp+=getBestMove(x,choose(move),compmove)
    return temp

def copy(a):
    z=[['_',"_","_"],["_","_","_"],["_","_","_"]]
    for i in range(0,3):
        for j in range(0,3):
            z[i][j]=a[i][j]
    return z


def computermove(a,move,compmove):
    value,x,y=-100000,0,0
    choose=lambda move:"X" if move=="O" else "O"
    for i in range (0,3):
        for j in range(0,3):
            if a[i][j]=="_":
                z=copy(a)
                z[i][j]=move
                temp=getBestMove(z,choose(move),compmove)
                if value<temp:
                    value=temp
                    x=i
                    y=j
    return(x,y)

    

def printa(a):
    for x in a:
        for y in x:
            print(y,end="")
        print()

a=[['_',"_","_"],["_","_","_"],["_","_","_"]]
move="X"


def clicked(r,c):
    if player(a,"X",r,c):
        winner=iswinner(a,"X")
        if winner==1:
            for i in range(3):
                for j in range(3):
                    b[i][j]["state"]="disabled"
            print("X"+" won the game")
        x,y=computermove(a,"O","O")
        a[x][y]="O"
        b[x][y].configure(text="O")
    

        winner=iswinner(a,"O")
        printa(a)
        if winner==1:
            for i in range(3):
                for j in range(3):
                    b[i][j]["state"]="disabled"
            print("O"+" won the game")




root=Tk()
root.title("Tic Tac Toe")
root.resizable(0,0)

b=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(3):
    for j in range(3):
                                          
        b[i][j] = Button(
                        height = 4, width = 8,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)

mainloop()