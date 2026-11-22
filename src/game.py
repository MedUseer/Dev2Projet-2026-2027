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

# temp MVP classes for testing
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

        for row in range(self.height):
            grid.append([])
            for col in range(self.width):
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

class Instruction:
    def __init__(self, reapeat_count:int, children_instructions : list, type : instructions_type = "forward") :
        self.type = type
        self.reapeat_count = reapeat_count
        self.children_instructions = children_instructions

     #  instruction list format --> instruction = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
     
     #methods

class Program:
    
    def __init__(self, instructions: list, failed_step:int = 0, current_step:int = 0, error_message:str = ""):
        self.instructions = instructions
        self.failed_step = failed_step
        self.current_step = current_step
        self.error_message = error_message
    
     #methods
    
    def run_all(self) -> bool:
        """
        Execute all program instructions in order until completion or an error occurs.

        PRE:
            - The program has at least one instructions (self.instructions is non-empty).
            - The associated robot and level (grid, walls, gems, goal) are properly initialized.
        POST:
            - Sequentially executes all instructions in the program (RM-03).
            - Updates the robot's state (position, direction) and execution state (current_step, failed_step, error_message).
            - Stops if the robot hits a wall (RM-06) or goes out of bounds of the grid (RM-01).
            - Returns True if everything succeeds, False if an error occurs.
        """
        pass
    
    def run_step_by_step(self) -> bool:
        """
        Execute a single program instruction at the current step (current_step).

        PRE:
            - current_step must be a valid integer between 0 and len(self.instructions) - 1 (inclusive).
            - The robot and level are initialized.
        POST:
            - Executes the instruction pointed to by self.current_step (RM-03).
            - Increments self.current_step by 1 if instruction execution succeeds.
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
    # Init clockwise direction
    clockwise_direction = ["up", "right", "down", "left"]       
    
    def __init__(self, current_position : Position, direction : dico_direction = "up"):
        if direction not in dico_direction :
            raise ValueError(f"Direction invalide : {direction}")
        self.current_position = current_position
        self.direction = direction
        self.collect_gems = 0
    
    #methods
    
    def get_direction_symbol(self) -> str:
        """
        
        """
        return dico_direction[self.direction]
    
    def get_next_position(self) -> Position:
        """
        
        """
        row = self.current_position.row
        col = self.current_position.column    
    
        if self.direction == "up":
            row -= 1
        elif self.direction == "down":
            row += 1
        elif self.direction == "left":
            col -= 1
        elif self.direction == "right":
            col += 1
            
        return Position(row, col)
    
    def move_forward(self) -> bool:
        """

        """
        self.current_position = self.get_next_position()

    def turn_left(self) -> bool:
        """

        """
        idx = self.clockwise_direction.index(self.direction)
        self.direction = self.clockwise_direction[(idx - 1) % 4]    # formula magic with list clockwise_direction, ( 0(= up) - 1 ) % 4 = -1 % 4 = 3(= left)

    def turn_right(self) -> bool:
        """

        """
        idx = self.clockwise_direction.index(self.direction)
        self.direction = self.clockwise_direction[(idx + 1) % 4]

    def collect_gems(self, type_cells: dico_type_cells) -> bool:
        """

        """
        if type_cells == "gem":
            self.collect_gems += 1
            return True
        return False
    

if __name__ == "__main__" :
    
    raw_instruction = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
    
    prog = Program(raw_instruction, failed_step=0, current_step=0, error_message="")
    print(prog.instructions)
    
    # print(dico_type_cells)
    # print(dico_direction)
    # print(instructions_type)