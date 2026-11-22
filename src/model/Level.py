class Level:
    """Represent a level"""
    
    def __init__(self) -> None:
    
        self.__title = ""
        self.__grid = [[]]
        self.__start_position = start_position
        self.__arrival_position = arrival_position
        self.__allowed_instructions = allowed_instructions
        self.__max_instructions = max_instructions
        self.__reference_solution_instructions = reference_solution_instructions
        self.__gems_count = gems_count
        self.__walls_count = walls_count
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self,value) -> None:
        self.__title = value