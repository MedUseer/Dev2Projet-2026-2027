import emoji # import the emoji library for display.

dico_type_cells = {
        "gem": "\033[32m▪\033[0m", # code ANSI
        "wall" : emoji.emojize(":rock:"),
        "robot" : emoji.emojize(":robot:"),
        "arrival":emoji.emojize(":round_pushpin:"),
        "empty":"_"
} #

"""
MEMO tech - type of cells

- 📍 --> symbol for arrival

- 🪨 -> symbol for wall

- 🤖 -> symbole for start/robot

- ▪ (green)-> symbol for gem


design example for grid
|_| |_| |_|
|_| |_| |_|
|_| |_| |_|

gem - > U+1F7E9 code unicode


"""
# MVP - version 1

class Position:

    def __init__(self,row : int,column : int):
        self.row = row
        self.column = column

    #methods
    
    def get_row(self):
        """
            doc soon ...
        """
        return self.row
    
    def get_column(self):
        """
            doc soon ...
        """
        return self.column


class Cell:
    
    def __init__(self,position : Position,type="empty"):
        self.position = position
        self.type = type

    #methods
    def get_type(self):
        """
            doc soon ...
        """
        return self.type


class Grid:

    def __init__(self,width : int,height : int):

        self.width = width
        self.height = height
        self.grid = Grid

    #methods

    def get_init_grid(self):
    
        """
            doc soon ...
        """
        grid = []

        for row in range(self.width):
            grid.append([])
            for col in range(self.height):
                position_cell = Position(row,col) # create a position cell
                cell = Cell(position_cell,"empty") # create a cell
                grid[row].append(cell) # add each cell on array
                
        self.grid = grid 

        return self.grid

    def set_element_position(self,row : int ,col : int,new_type : dico_type_cells = "empty" ):    

        """
            doc soon ...
        """
        if new_type != "empty":
            self.grid[row][col].type = new_type # change the type
        
        return  f"| {dico_type_cells[self.grid[row][col].type]} |"

