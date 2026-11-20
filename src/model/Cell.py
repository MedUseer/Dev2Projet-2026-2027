class Cell:
    """Represent one cell of the grid."""
    
    def __init__(self,type_cell : str = "empty") -> None:
        self.__type_cell = type_cell 
    
    @property
    def type_cell(self) -> str:
        """return type of cell
            PRE: nothing
            POST: return a String which is the type of cell
        """
        return self.__type_cell

    @type_cell.setter
    def type_cell(self,value : str) -> None:
        """
        """
        self.__type_cell = value