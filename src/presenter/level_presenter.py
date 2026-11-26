from model.Level import Level
from model.Grid import Grid
from view.GameInterface import GameInterface

def parsing(element : str,spliter : str) -> tuple:
    elements : list = []
    
    for el in element.split(spliter):
        elements.append(int(el))

    return elements[0],elements[1]


def create_level(interface : GameInterface,level : Level) -> None:

    """
    """

    title = str(input("Titre du niveau : "))
    
    #error manage missed

    level.title = title # update the model
    interface.window.after(0,interface.create_header,title) # update view

    dimension = input("Dimensions pour la grille (ex. 5x5) : ").lower()
    #error manage missed
    width,height = parsing(dimension,"x")

    grid = Grid(width,height)
    grid.init_grid()

    interface.window.after(0,interface.create_grid,grid.grid)

    start_position = input("Position de départ du robot (ex. 2,2) : ")
    #error manage missed
    row_robot,col_robot = parsing(start_position,",")
    grid.grid[row_robot][col_robot].type_cell = "robot"
    interface.window.after(0,interface.create_grid,grid.grid)

    arrival_position = input("Position d'arriver du robot (ex. 0,0) : ")
    #error manage missed
    row_robot_arrival,col_robot_arrival = parsing(arrival_position,",")
    grid.grid[row_robot_arrival][col_robot_arrival].type_cell = "arrival"
    interface.window.after(0,interface.create_grid,grid.grid)

    gems_count = int(input("Nombres de gemmes à placer (ex. 3) : "))
    #error manage missed
    for g in range(1,gems_count+1):
        position_gem = input(f"Position pour la gemme n°{g} (ex.1,2) : ")
        row_gem,col_gem = parsing(position_gem,',')
        #error manage missed
        grid.grid[row_gem][col_gem].type_cell = "gem"
        interface.window.after(0,interface.create_grid,grid.grid)

    walls_count = int(input("Nombres de murs à place (ex.2) : "))
    #error manage missed
    for w in range(1,walls_count+1):
        position_wall = input(f"Position pour la gemme n°{w} (ex.1,2) : ")
        row_wall,col_wall = parsing(position_wall,',')
        #error manage missed
        grid.grid[row_wall][col_wall].type_cell = "wall"
        interface.window.after(0,interface.create_grid,grid.grid)
