from model import Cell as c # import Cell module 

class Grid:
    """Represent a grid"""
    def __init__(self,height : int = 5,width : int = 5) -> None:

        self.__height = height
        self.__width = width
        self.grid = []
        
    @property
    def height(self) -> int:
        """
            PRE:
            POST:
        """
        return self.__height

    @property
    def width(self) -> int:
        """
            PRE:
            POST:
        """
        return self.__width

    def init_grid(self) -> None:
        """Init the grid with cell

            PRE:
            POST:
        """

        for row in range(self.__height):
            self.grid.append([])

            for col in range(self.__width):
                cell = c.Cell() # create a cell
                self.grid[row].append(cell)

    def change_type_cell(self,row : int, col : int, new_type_cell) -> None:
        """
            PRE:
            POST:
        """
        grid = self.grid
        grid[row][col].type_cell = new_type_cell # change type of cell

        