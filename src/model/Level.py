class Level:
    """Represent a level"""

    def __init__(self) -> None:
    
        self.__title = ""
        self.__grid = [[]]
        
        self.__start_position = (4,0)
        self.__arrival_position = (0,0)
        self.__allowed_instructions = []
        self.__max_instructions = 10
        self.__reference_solution_instructions_count = 5
        self.__gems_count = 3
        self.__walls_count = 5
        
    @property
    def title(self) -> str:
        return self.__title
    @title.setter
    def title(self, value) -> None:
        self.__title = value

    @property
    def grid(self) -> list[list]:
        return self.__grid
    @grid.setter
    def grid(self, value : list[list]) -> None:
        self.__grid = value

    @property
    def start_position(self) -> tuple:
        return self.__start_position
    @start_position.setter
    def start_position(self, value : tuple) -> None:
        self.__start_position = value

    @property
    def arrival_position(self) -> tuple:
        return self.__arrival_position
    @arrival_position.setter
    def arrival_position(self, value : tuple) -> None:
        self.__arrival_position = value

    @property
    def allowed_instructions(self) -> list[list]:
        return self.__allowed_instructions
    @allowed_instructions.setter
    def allowed_instructions(self,value : list) -> None:
        self.__allowed_instructions = value
    
    @property
    def max_instructions(self) -> int:
        return self.__max_instructions
    @max_instructions.setter
    def max_instructions(self, value : int) -> None:
        self.__max_instructions = value

    @property
    def reference_solution_instructions_count(self) -> int:
        return self.__reference_solution_instructions_count
    @reference_solution_instructions_count.setter
    def reference_solution_instructions_count(self, value : int) -> None:
        self.__reference_solution_instructions_count = value

    @property
    def gems_count(self) -> int:
        return self.__gems_count
    @gems_count.setter
    def gems_count(self, value : int) -> None:
        self.__gems_count = value

    @property
    def walls_count(self) -> int:
        return self.__walls_count
    @walls_count.setter
    def walls_count(self, value : int) -> None:
        self.__walls_count = value