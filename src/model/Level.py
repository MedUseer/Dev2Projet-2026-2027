class Level:
    """Represent a level"""

    def __init__(self) -> None:
    
        self.__title = ""
        self.__grid = [[]]
        
        self.__start_position = (4,0)
        self.__arrival_position = (0,0)
        self.__allowed_instructions = []
        self.__max_instructions = 10
        self.__reference_solution_instructions = 5
        self.__gems_count = 3
        self.__walls_count = 5
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self,value) -> None:
        self.__title = value