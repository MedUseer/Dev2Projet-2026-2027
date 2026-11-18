class Grid:
    """Represent a grid"""
    def __init__(self,height : int,width : int) -> None:

        self.__height = height
        self.__width = width
        self.grid = [[]]
        
    @property
    def height(self) -> int:
        """
        """
        return self.__height

    @property
    def width(self) -> int:
        """
        """
        return self.__width

