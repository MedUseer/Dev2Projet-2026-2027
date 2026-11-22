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
    """
    Temporary class Position, used only for local testing of F-03; replace when merging the code
    """
    def __init__(self,row : int,column : int):
        self.row = row
        self.column = column

    #methods
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column


class Cell:
    """
    Temporary class Cell, used only for local testing of F-03; replace when merging the code
    """    
    def __init__(self,position : Position,type : dico_type_cells = "empty"):
        self.position = position
        self.type = type

    #methods
    def get_type(self):
        return self.type


class Grid:
    """
    Temporary class Grid, used only for local testing of F-03; replace when merging the code
    """
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

class Level:
    """
    Temporary class Level, used only for local testing of F-03; replace when merging the code
    """
    def __init__(self, grid: Grid, start_position: Position, arrival_position: Position):
        self.grid = grid
        self.start_position = start_position
        self.arrival_position = arrival_position

    def is_position_valid(self, position: Position) -> bool:
        row = position.get_row()
        col = position.get_column()
        if not (0 <= row < self.grid.height and 0 <= col < self.grid.width):
            return False
        return self.grid.grid[row][col].get_type() != "wall"




#   ===== Execution Classes =====
class Robot:
    # Init clockwise direction
    __clockwise_direction = ["up", "right", "down", "left"]       
    
    def __init__(self, current_position : Position, direction : dico_direction = "up"):
        if direction not in dico_direction :
            raise ValueError(f"Direction invalide : {direction}")
        self.__current_position = current_position
        self.__direction = direction
        self.__collected_gems = 0
    
    #properties
    @property
    def current_position(self) -> Position:
        return self.__current_position
    
    @current_position.setter
    def current_position(self, new_position: Position):
        self.__current_position = new_position
    
    @property
    def direction(self) -> str:
        return self.__direction
    
    @direction.setter
    def direction(self, new_direction: str):
        if new_direction not in dico_direction:
            raise ValueError(f"Direction invalide : {new_direction}")
        self.__direction = new_direction
    
    @property
    def collected_gems(self) -> int:
        return self.__collected_gems
    
    #methods
    def get_direction_symbol(self) -> str:
        """
        
        """
        return dico_direction[self.__direction]
    
    def get_next_position(self) -> Position:
        """
        
        """
        row = self.current_position.row
        col = self.current_position.column    
    
        if self.__direction == "up":
            row -= 1
        elif self.__direction == "down":
            row += 1
        elif self.__direction == "left":
            col -= 1
        elif self.__direction == "right":
            col += 1
            
        return Position(row, col)
    
    def move_forward(self) -> bool:
        """

        """
        self.__current_position = self.get_next_position()
        return True

    def turn_left(self) -> bool:
        """

        """
        idx = self.__clockwise_direction.index(self.__direction)
        self.__direction = self.__clockwise_direction[(idx - 1) % 4]    # formula magic for clockwise, ( 0(= up) - 1 ) % 4 = -1 % 4 = 3(= left)
        return True

    def turn_right(self) -> bool:
        """

        """
        idx = self.__clockwise_direction.index(self.__direction)
        self.__direction = self.__clockwise_direction[(idx + 1) % 4]
        return True

    def collect_gems(self, type_cells: dico_type_cells) -> bool:
        """

        """
        if type_cells == "gem":
            self.__collected_gems += 1
            return True
        return False

class Instruction:
    def __init__(self, repeat_count:int, children_instructions : list, type : instructions_type = "forward") :
        self.type = type
        self.repeat_count = repeat_count
        self.children_instructions = children_instructions

     #  instruction list format --> instruction = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
     
     #methods

class Program:
    
    def __init__(self, robot : Robot, level : Level, instructions=None):
        self.__robot = robot
        self.__level = level
        if instructions is not None:
            self.__instructions = instructions
        else :
            self.__instructions = []
        self.__failed_step = None
        self.__current_step = 0
        self.__error_message = ""
    
    #properties
    @property
    def robot(self) -> Robot:
        return self.__robot
    
    @property
    def level(self) -> Level:
        return self.__level
    
    @property
    def instructions(self) -> list:
        return self.__instructions
    
    @instructions.setter
    def instructions(self, new_instructions: list):
        self.__instructions = new_instructions
    
    @property
    def failed_step(self):
        return self.__failed_step
    
    @property
    def current_step(self) -> int:
        return self.__current_step
    
    @current_step.setter
    def current_step(self, step: int):
        self.__current_step = step
        
    @property
    def error_message(self) -> str:
        return self.__error_message
    
    @error_message.setter
    def error_message(self, message: str):
        self.__error_message = message
    
    #methods
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
    
    def reached(self) -> bool:
        """
        Check whether the robot has reached the level's goal position (arrival_position).

        PRE:
            - The level has a defined goal cell (arrival_position / RM-08).
            - The robot's current position (robot.current_position) is initialized.
        POST:
            - Compares the robot's current position with the level's goal cell (D-01.3).
            - Returns True if the coordinates match exactly, False otherwise.
            Excptions:
                - Raises TypeError if robot or robot.current_position is not defined (None).
                - Raises ValueError if level has no arrival_position configured (None).
        """
        if self.__robot is None or self.__robot.current_position is None:
            raise TypeError("The robot's position is undefined.")
        if self.__level is None or self.__level.arrival_position is None:
            raise ValueError("No arrival point!")
        
        return (
            self.__robot.current_position.get_row() == self.__level.arrival_position.get_row()
            and
            self.__robot.current_position.get_column() == self.__level.arrival_position.get_column()
        )
    

if __name__ == "__main__" :
    
    # 5x5，depart (4, 0)，arrival (3, 1)， gem(3, 0)）
    grid = Grid(5, 5)
    grid.get_init_grid()
    grid.set_element_position(3, 0, "gem")
    grid.set_element_position(2, 2, "wall")
    grid.set_element_position(3, 1, "arrival")

    level = Level(grid, start_position=Position(4, 0), arrival_position=Position(3, 1))
    robot = Robot(current_position=Position(4, 0), direction="up")

    raw_instructions = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
    prog = Program(robot=robot, level=level, instructions=raw_instructions)

    print("=== 1. Init ===")
    print(prog.instructions)
    print(f"robot pos init: ({robot.current_position.get_row()}, {robot.current_position.get_column()}) {robot.get_direction_symbol()}")
    print("reached?:", prog.reached())  # -> False

    print("\n=== 2. forward and collect ===")
    robot.move_forward()  # (4, 0) -> (3, 0)
    print(f"pos after forward: ({robot.current_position.get_row()}, {robot.current_position.get_column()}) {robot.get_direction_symbol()}")
    cell_type = level.grid.grid[robot.current_position.get_row()][robot.current_position.get_column()].get_type() 
    print(cell_type) # type of (3, 0) -> gem
    print("got gem?:", robot.collect_gems(cell_type), "| gems collected:", robot.collected_gems)

    print("\n=== 3. turn right, left and reached ===")
    robot.turn_right()    # up -> right
    print("direction after turn right:", robot.direction, robot.get_direction_symbol())
    robot.move_forward()  # (3, 0) -> (3, 1) arrival
    print(f"pos after forward: ({robot.current_position.get_row()}, {robot.current_position.get_column()}) {robot.get_direction_symbol()}")
    print("reached? :", prog.reached())  # -> True

    robot.turn_left()     # right -> up
    print("direction after turn left:", robot.direction, robot.get_direction_symbol())