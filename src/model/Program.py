from model.Robot import Robot
from model.Level import Level

class Program:
    
    def __init__(self, robot : Robot, level : Level, instructions: list = None):
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
            # Execute the current step and check if it succeeded
            step_succeeded = self.run_step_by_step()
            if not step_succeeded :
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
    
    def reset(self, new_Level : Level) -> None:
        """
        Reset the level, robot position/state, and execution progress while keeping instructions.
        
        PRE:
            - new_Level is a re-loaded/initialized Level instance with a valid start_position.
        POST:
            - Replaces self.__level with new_Level.
            - Resets execution state: current_step = 0, failed_step = None, error_message = "".
            - If self.__robot is not None, resets its position to start_position, direction to "up", and collected_gems to 0.
            - Preserves self.__instructions unchanged so the player can edit and re-run the program.
        """
        self.__level = new_Level
        self.__current_step = 0
        self.__failed_step = None
        self.__error_message = ""
        
        if self.__robot is not None:
            self.__robot.current_position = self.__level.start_position
            self.__robot.direction = "up"
            self.__robot.reset_gems()