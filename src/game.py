import emoji

instructions_type = {
    "forward": emoji.emojize(":footprints:"),
    "turn_left": emoji.emojize(":left_arrow:"),
    "turn_right": emoji.emojize(":right_arrow:"),
    "collect": emoji.emojize(":raised_hand:"),
    "repeat": emoji.emojize(":counterclockwise_arrows_button:"),
}

dico_direction = {
    "up": emoji.emojize(":up_arrow:", variant="text_type"),
    "down": emoji.emojize(":down_arrow:", variant="text_type"),
    "right": emoji.emojize(":right_arrow:", variant="text_type"),
    "left": emoji.emojize(":left_arrow:", variant="text_type"),
}

dico_type_cells = {
        "gem": "\033[32m▪\033[0m", # code ANSI
        "wall" : emoji.emojize(":rock:"),
        "robot" : emoji.emojize(":robot:"),
        "arrival":emoji.emojize(":round_pushpin:"),
        "empty":"_"
} 


class Position:

    def __init__(self,row : int,column : int):
        self.row = row
        self.column = column

    #methods
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column


class Cell:
    
    def __init__(self,position : Position,type : dico_type_cells = "empty"):
        self.position = position
        self.type = type

    #methods
    def get_type(self):
        return self.type


class Grid:

    def __init__(self,width:int = 5,height:int = 5 ):

        self.width = width
        self.height = height
        self.grid = Grid

    #methods

    def get_init_grid(self):
    
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

        if new_type != "empty":
            self.grid[row][col].type = new_type # change the type of cell Object
        
        return  f"| {dico_type_cells[self.grid[row][col].type]} |" 



#   ===== Execution Classes =====

class Insturction:
    def __init__(self, reapeat_count:int, children_instructions : list, type : instructions_type = "forward") :
        self.type = type
        self.reapeat_count = reapeat_count
        self.children_instructions = children_instructions

class Program:
    
    def __init__(self, insturctions: list, failed_step:int, current_step:int, error_message:str):
        self.insturctions = insturctions
        self.failed_step = failed_step
        self.current_step = current_step
        self.error_message = error_message
    
     #methods
    
    def run_all(self) -> bool:
        """
        Execute all program insturctions in order until completion or an error occurs.

        PRE:
            - The program has at least one insturction (self.insturctions is non-empty).
            - The associated robot and level (grid, walls, gems, goal) are properly initialized.
        POST:
            - Sequentially executes all insturctions in the program (RM-03).
            - Updates the robot's state (position, direction) and execution state (current_step, failed_step, error_message).
            - Stops if the robot hits a wall (RM-06) or goes out of bounds of the grid (RM-01).
            - Returns True if everything succeeds, False if an error occurs.
        """
        print(f"{self.insturctions}") 
    
    def run_step_by_step(self) -> bool:
        """
        Execute a single program insturction at the current step (current_step).

        PRE:
            - current_step must be a valid integer between 0 and len(self.insturctions) - 1 (inclusive).
            - The robot and level are initialized.
        POST:
            - Executes the insturction pointed to by self.current_step (RM-03).
            - Increments self.current_step by 1 if insturction execution succeeds.
            - Updates failed_step and error_message if a collision (RM-06) or going out of bounds occurs.
            - Returns True if the step succeeds, False if blocked or on failure.
        """
        pass
    
    def reached(self) -> bool:
        """
        Check whether the robot has reached the level's goal position (arrival_position).

        PRE:
            - The level has a defined goal cell (arrival_position / RM-08).
            - The robot's current position (robot.current_position) must be initialized.
        POST:
            - Compares the robot's current position with the level's goal cell (D-01.3).
            - Returns True if the coordinates match exactly, False otherwise.
        """
        pass


class Robot:
    def __init__(self, current_position, direction : dico_direction = "up"):
        self.current_position = current_position
        self.direction = direction
    
    #methods
    
    def move_forward(self):
        """

        PRE:
            - 
        POST:
            -
        """
        pass

    def turn_left(self):
        """

        PRE:
            - 
        POST:
            -
        """
        
        
        pass

    def turn_right(self):
        """

        PRE:
            - 
        POST:
            -
        """
        pass

    def collect_gems(self, type_cells: dico_type_cells = "gem"):
        """

        PRE:
            - 
        POST:
            -
        """
        pass
    

if __name__ == "__main__" :
    
    instruction = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
    
    prog = Program(instruction, failed_step=0, current_step=0, error_message="")
    print(prog.insturctions)
    prog.run_all()
    
    print(dico_type_cells)
    print(dico_direction)
    print(instructions_type)