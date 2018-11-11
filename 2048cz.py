from tkinter import *
from random import *

def new_game(n):
    matrix = [[0]*n for i in range(n)]
    return matrix

def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==2048:
                return 'win'
    for i in range(len(mat)-1): 
        for j in range(len(mat[0])-1): 
            if mat[i][j]==mat[i+1][j] or mat[i][j+1]==mat[i][j]:
                return 'not over'
    for i in range(len(mat)): 
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                return 'not over'
    for k in range(len(mat)-1): 
        if mat[len(mat)-1][k]==mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1): 
        if mat[j][len(mat)-1]==mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'

def reverse(mat):
    new=[]
    x=y=len(mat)
    for i in range(x):
        new.append([])
        for j in range(y):
            new[i].append(mat[i][y-j-1])
    return new

def transpose(mat):
    new=[]
    x=y=len(mat)
    for i in range(y):
        new.append([])
        for j in range(x):
            new[i].append(mat[j][i])
    return new

def cover_up(mat):
    x=y=len(mat)
    new=[x*[0] for i in range(y)]
    done=False
    for i in range(x):
        count=0
        for j in range(y):
            if mat[i][j]!=0:
                new[i][count]=mat[i][j]
                if j!=count:
                    done=True
                count+=1
    return (new,done)

def merge(mat):
    done=False
    x=y=len(mat)
    for i in range(x):
         for j in range(y-1):
             if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                 mat[i][j]*=2
                 mat[i][j+1]=0
                 done=True
    return (mat,done)

def up(game):
        game=transpose(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=transpose(game)
        return (game,done)

def down(game):
        game=reverse(transpose(game))
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=transpose(reverse(game))
        return (game,done)

def left(game):
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        return (game,done)

def right(game):
        game=reverse(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=reverse(game)
        return (game,done)