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
            "arrival" : 'ARRIVER',
            'gem' : '🟢',
            'wall' : '🧱'
        }
        self.frame_header = tk.Frame(self.window,relief="ridge",borderwidth=5,width=600,height=200)
        self.frame_main = tk.Frame(self.window,relief="ridge",borderwidth=5,width=600,height=400)
        self.frame_footer = tk.Frame(self.window,relief="ridge",borderwidth=5,width=600,height=200)
        
    def create_header(self,title : str, get_state_level : str) -> None:
        self.frame_header.pack_propagate(False)
        self.frame_header.config(bg="blue")
        
        btn_state_level = tk.Button(self.frame_header,text="status du niveau",command=get_state_level)#button for show the stateful of current level
        title = tk.Label(self.frame_header,text=title,font=self.font_text,bg="blue") # title
        instructions_count = tk.Label(self.frame_header,text="instructions en cours 0/10",font=self.font_text,bg="blue") #instructions ...

        #positionning
        self.frame_header.pack()#relx=0.5,rely=0,anchor="n",width=600,height=200
        btn_state_level.pack(pady=15,side="left")
        title.pack(pady=20)
        instructions_count.pack(padx=10,side="right")

    def create_grid(self,grid : Grid) -> None:

        self.frame_main.pack_propagate(False)
        self.frame_main.config(bg="red")
        frame_grid = tk.Frame(self.frame_main,relief="ridge",borderwidth=6) # create frame for the grid

        #positionning
        frame_grid.config(bg="green")
        self.frame_main.pack()#relx=0,rely=0.5,anchor="center",width=600,height=300
        frame_grid.place(relx=0,rely=0.5,anchor="w",x=10)        

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                cell = tk.Label(frame_grid,text=self.type_cells[grid[row][col].type_cell],width=6,height=3,relief="ridge") # create a cell            
                cell.config(bg="white")
                cell.grid(row=row,column=col)