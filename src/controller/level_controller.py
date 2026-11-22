from model.Level import Level
from model.Grid import Grid
from view.GameInterface import GameInterface

def create_level(interface : GameInterface,level : Level) -> None:

    """
    """

    title = str(input("Titre du niveau : "))
    
    #error manage missed

    level.title = title # update the model
    interface.window.after(0,interface.create_header,title) # update view

    dimension = input("Dimensions pour la grille (ex. 5x5) : ").lower()
    #error manage missed
    width,height = dimension.split('x')
    
    grid = Grid(int(width),int(height))
    grid.init_grid()

    interface.window.after(0,interface.create_grid,grid.grid)
