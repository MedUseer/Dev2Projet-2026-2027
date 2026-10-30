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

    def __init__(self,width:int = 5,height:int = 5 ):

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
            self.grid[row][col].type = new_type # change the type of cell Object
        
        return  f"| {dico_type_cells[self.grid[row][col].type]} |" 

class Level:

    def __init__(self,title : str,grid : Grid,start_position : Position,arrival_position : Position
    ,allowed_instructions : list,instructions_count : int,max_instructions:int, reference_solution_instructions : int, gems_count : int,
    walls_count : int):

        self.title = title
        self.grid = grid
        self.start_position = start_position
        self.arrival_position = arrival_position
        self.allowed_instructions = allowed_instructions
        self.instructions_count = instructions_count
        self.max_instructions = max_instructions
        self.reference_solution_instructions = reference_solution_instructions
        self.gems_count = gems_count
        self.walls_count = walls_count

    #methods ...

class GameInterface:

    def __init__(self,level:Level):
        self.level = level

    #methods
    def get_grid(self):
        return self.level.grid.grid

    def display_grid(self):

        grid = self.level.grid.grid
        compteur = 0
        for row in range(len(grid)):

            for col in range(len(grid[row])):
                
                    print(self.level.grid.set_element_position(row,col),end=' ')
            if compteur < len(self.level.allowed_instructions):
                print('  '*4+self.level.allowed_instructions[compteur],end='')
                compteur+=1

            print("\n")

   def display_level(self):

        print("\n"+10*' '+self.level.title+"\n\n")
        self.display_grid() #The display is not optimized for grids smaller than 5×5.

        # button run complete and run step by step
        print("\n",emoji.emojize(":play_button:")," lancement complet") 
        print("\n",emoji.emojize(":gear:")," pas suivant","\n")