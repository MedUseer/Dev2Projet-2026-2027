import tkinter as tk
from tkinter import font as tf
from model.Grid import Grid #import the model

class GameInterface:
    """Represent a GUI interface"""

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.font_text = tf.Font(family="Poppins",size=15)
        self.type_cells = {
            "" : "",
            "robot":'🤖',
            "arrival" : 'ARRIVER'
        }

    def create_header(self,title):

        frame_header = tk.Frame(self.window,bg="red")
        title = tk.Label(frame_header,text=title,font=self.font_text,bg="blue") # title
        instructions_count = tk.Label(frame_header,text="instructions en cours 0/10",font=self.font_text,bg="blue")#instructions ...
        frame_header.place(relx=0.5,rely=0,anchor="n",width=600,height=200)
        title.pack(pady=20)
        instructions_count.pack(padx=10,side="right")

    def create_grid(self,grid : Grid) -> None:

        frame_grid = tk.Frame(self.window,relief="ridge",borderwidth=4) # create frame for the grid
        frame_grid.place(relx=0,rely=0.5,anchor="w",x=10)        

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                cell = tk.Label(frame_grid,text=self.type_cells[grid[row][col].type_cell],width=6,height=3,relief="ridge") # create a cell            
                cell.config(bg="white")
                cell.grid(row=row,column=col)
