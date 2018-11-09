#coding=UTF-8

from Tkinter import *
from random import randint
from random import choice
import tkMessageBox

if __name__ == '__main__':
    root = Tk()
    # game = Game(root)
    # game.mainloop()

class Grid(object):
    def __init__(self, master=None, height=4, width=4, offset=10, grid_width=200, bg="#696969"):
        self.height = height
        self.width = width
        self.offset = offset
        self.grid_width = grid_width
        self.bg = bg
        self.canvas = Canvas(master, width=self.width*self.grid_width + 2*self.offset,height=self.height*self.grid_width+2*self.offset, bg=self.bg)
        self.initial()

        def initial(self):
            for i in range(0,4):
                for j in range(0,4):
                    x = i * self.grid_width + self.offset
                    y = j * self.grid_width + self.offset
                    self.canvas.create_rectangle(x+10, y+10, x + self.grid_width-10, y + self.grid_width-10, fill="#808080",outline=self.bg)
            self.canvas.pack(side=RIGHT, fill=Y)

        def draw(self, pos, color, text):
            x = pos[0] * self.grid_width + self.offset
            y = pos[1] * self.grid_width + self.offset
            # outline属性要与网格的背景色（self.bg）相同，要不然会很丑
            self.canvas.create_rectangle(x+10, y+10, x + self.grid_width-10, y + self.grid_width-10, fill=color, outline=self.bg)
            ft1 = ('Comic Sans MS', 50, "bold")
            self.canvas.create_text(pos[0] * 200 + 110, pos[1] * 200 + 110, text=text, font=ft1)


