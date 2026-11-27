class Robot:  
    """Represent a Robot"""
    
    DIRECTION_SYMBOLS = {
        "up": "⬆︎",
        "down": "⬇︎",
        "right": "➡︎",
        "left": "⬅︎",
    }
    
    def __init__(self, current_position : tuple[int, int], direction : str = "up") -> None:
        if direction not in self.DIRECTION_SYMBOLS:
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
        if new_direction not in self.DIRECTION_SYMBOLS:
            raise ValueError(f"Direction invalide : {new_direction}")
        self.__direction = new_direction
    
    @property
    def collected_gems(self) -> int:
        return self.__collected_gems
    
    #methods
    def get_direction_symbol(self) -> str:
        return self.DIRECTION_SYMBOLS[self.__direction]
    
    def get_next_position(self) -> tuple[int, int]:
        """
        Calculate the robot's next coordinates.
        
        PRE:
            - self.__current_position is a valid (row, col) tuple of integers.
            - self.__direction is a valid key in dico_direction ("up", "down", "left", "right").
        POST:
            - Returns the target (row, col) tuple one cell ahead in the current direction.
            - Does not modify self.__current_position (used for collision/bounds pre-checking).
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
        Move the robot one cell forward in its current direction. (EF-03.3)
        
        PRE:
            - The target position has already been validated (within grid bounds and not a wall).
        POST:
            - Updates self.__current_position to the coordinates returned by get_next_position().
            - Leaves self.__direction unchanged.
            - Returns True.
        """
        self.__current_position = self.get_next_position()
        return True

    def turn_left(self) -> bool:
        """
        Rotate the robot 90 degrees to the left. (EF-03.4)
        
        PRE:
            - self.__direction is initialized.
        POST:
            - Updates self.__direction counterclockwise (up -> left -> down -> right -> up).
            - Leaves self.__current_position unchanged.
            - Returns True if the direction is valid and updated, False otherwise.
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
        Rotate the robot 90 degrees to the right. (EF-03.5)
        
        PRE:
            - self.__direction is initialized.
        POST:
            - Updates self.__direction clockwise (up -> right -> down -> left -> up).
            - Leaves self.__current_position unchanged.
            - Returns True if the direction is valid and updated, False otherwise.
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
        Try to collect a gem based on the current cell's type (RM-07).

        PRE:
            - type_cells is a string representing the type of the robot's current cell.
        POST:
            - If type_cells == "gem", increments self.__collected_gems by 1 and returns True.
            - Otherwise, leaves self.__collected_gems unchanged and returns False.
            - Does not modify the grid cell itself.
        """
        if type_cells == "gem":
            self.__collected_gems += 1
            return True
        return False
    
    def reset_gems(self) -> None:
        self.__collected_gems = 0