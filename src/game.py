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
class Cell:
    """
    Temporary class Cell, used only for local testing of F-03; replace when merging the code
    """    
    def __init__(self, type_cell : str = "empty") -> None:
        self.__type_cell = type_cell

    #properties
    @property
    def type_cell (self) -> str:
        return self.__type_cell
    @type_cell.setter
    def type_cell(self, value: str) -> None:
        self.__type_cell = value

class Grid:
    """
    Temporary class Grid, used only for local testing of F-03; replace when merging the code
    """
    def __init__(self,width:int = 5,height:int = 5 ) -> None:

        self.__height = height
        self.__width = width
        self.grid = []

    #properties
    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    #methods
    def init_grid(self) -> None:
        """Init the grid with cell"""
        for row in range(self.__height):
            self.grid.append([])
            for col in range(self.__width):
                cell = Cell()  
                cell.type_cell = "empty" 
                self.grid[row].append(cell)

class Level:
    """
    Temporary class Level, used only for local testing of F-03; replace when merging the code
    """
    def __init__(self) -> None:
        self.grid = [[]]
        self.start_position = (4, 0)
        self.arrival_position = (0, 0)

    #properties
    @property
    def grid(self) -> list[list]:
        return self.__grid
    @grid.setter
    def grid(self, value: list[list]) -> None:
        self.__grid = value

    @property
    def start_position(self) -> tuple:
        return self.__start_position
    @start_position.setter
    def start_position(self, value: tuple) -> None:
        self.__start_position = value

    @property
    def arrival_position(self) -> tuple:
        return self.__arrival_position
    @arrival_position.setter
    def arrival_position(self, value: tuple) -> None:
        self.__arrival_position = value



#   ===== Execution Classes =====
class Robot:  
    
    def __init__(self, current_position : tuple[int, int], direction : str = "up") -> None:
        if direction not in dico_direction :
            raise ValueError(f"Direction invalide : {direction}")
        self.__current_position = current_position
        self.__direction = direction
        self.__collected_gems = 0
    
    #properties
    @property
    def current_position(self) -> tuple[int, int]:
        return self.__current_position
    @current_position.setter
    def current_position(self, new_position: tuple[int, int]) -> None:
        self.__current_position = new_position
    
    @property
    def direction(self) -> str:
        return self.__direction
    @direction.setter
    def direction(self, new_direction: str) -> None:
        if new_direction not in dico_direction:
            raise ValueError(f"Direction invalide : {new_direction}")
        self.__direction = new_direction
    
    @property
    def collected_gems(self) -> int:
        return self.__collected_gems
    
    #methods
    def get_direction_symbol(self) -> str:
        return dico_direction[self.__direction]
    
    def get_next_position(self) -> tuple[int, int]:
        """
        
        """
        row, col = self.__current_position  

        match self.__direction :
            case "up" :
                row -= 1
            case "down":
                row += 1
            case "left" :
                col -= 1
            case "right" :
                col += 1
            
        return (row, col)
    
    def move_forward(self) -> bool:
        """

        """
        self.__current_position = self.get_next_position()
        return True

    def turn_left(self) -> bool:
        """

        """
        match self.__direction:
            case "up":
                self.__direction = "left"
            case "left":
                self.__direction = "down"
            case "down":
                self.__direction = "right"
            case "right":
                self.__direction = "up"
            case _:
                return False
        return True

    def turn_right(self) -> bool:
        """

        """
        match self.__direction:
            case "up":
                self.__direction = "right"
            case "right":
                self.__direction = "down"
            case "down":
                self.__direction = "left"
            case "left":
                self.__direction = "up"
            case _:
                return False
        return True

    def collect_gems(self, type_cells: str) -> bool:
        """

        """
        if type_cells == "gem":
            self.__collected_gems += 1
            return True
        return False

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
            - self.instructions is a list of instructions (may be empty).
            - The associated robot and level (grid, walls, gems, goal) are properly initialized.
        POST:
            - Sequentially executes all instructions in the program (RM-03).
            - Updates the robot's state (current_position, direction) and execution state (current_step, failed_step, error_message).
            - Stops immediately if the robot hits a wall (RM-06) or goes out of bounds of the grid (RM-01).
            - Returns True if all instructions succeed.
            - Returns False if the instruction list is empty (CA-03.4) or if an error occurs.
            Exceptions:
                - Raises TypeError if robot or level is None.
        """
        if self.__robot is None or self.__level is None:
            raise TypeError("Robot and level not initialized.")
        if not self.__instructions:
            return False
        
        while self.__current_step < len(self.__instructions):
            if not self.run_step_by_step():
                return False
            return True
    
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
        
        return self.__robot.current_position == self.__level.arrival_position
    

if __name__ == "__main__" :
    
    # 5x5，depart (4, 0)，arrival (3, 1)， gem(3, 0)）
    grid = Grid(5, 5)
    grid.init_grid()
    grid.grid[3][0].type_cell = "gem"
    grid.grid[2][2].type_cell = "wall"
    grid.grid[3][1].type_cell = "arrival"

    level = Level()
    level.grid = grid.grid          # list[list]
    level.start_position = (4, 0)
    level.arrival_position = (3, 1)
    
    robot = Robot(current_position=level.start_position, direction="up")

    raw_instructions = ["forward", "turn_left", "turn_right", "collect", [2, "forward"]]
    prog = Program(robot=robot, level=level, instructions=raw_instructions)


    def robot_status(r: Robot) -> str:
        return f"{r.current_position} {r.get_direction_symbol()}"

    print("=== 1. Init ===")
    print(prog.instructions)
    print("robot pos init:", robot_status(robot))
    print("reached?:", prog.reached())  # -> False


    print("\n=== 2. forward and collect ===")
    robot.move_forward()  # (4, 0) -> (3, 0)
    print("pos after forward:", robot_status(robot))
    row, col = robot.current_position
    cell_type = level.grid[row][col].type_cell 
    print(cell_type)  # type of (3, 0) -> gem
    print("got gem?:", robot.collect_gems(cell_type), "| gems collected:", robot.collected_gems)


    print("\n=== 3. turn right, left and reached ===")
    robot.turn_right()    # up -> right
    print("direction after turn right:", robot.direction, robot.get_direction_symbol())
    
    robot.move_forward()  # (3, 0) -> (3, 1) arrival
    print("pos after forward:", robot_status(robot))
    
    robot.turn_left()     # right -> up
    print("direction after turn left:", robot.direction, robot.get_direction_symbol())
    print("reached? :", prog.reached())  # -> True
    
    
    print("\n=== 4. gem status and reset ===")
    print("is collected gem still in grid? :", grid.grid[3][0].type_cell)   # type of (3, 0) -> empty