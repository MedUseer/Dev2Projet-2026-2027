class Level:
    """Temporary class Level, used only for local testing of F-04;
    replace when merging the code."""

    def __init__(self, max_instructions: int = 10,
                 reference_solution_instructions_count: int = 5) -> None:
        self.max_instructions = max_instructions
        self.reference_solution_instructions_count = reference_solution_instructions_count

class LevelResult: 
    """represent the result of a level completed by a player"""

    def __init__(self, title: str = "", completed: bool = False, instructions_count: int = 0) -> None:

        self.__title = title
        self.__completed = completed
        self.__instructions_count = instructions_count
        self.__stars_count = 0

    @property 
    def title(self) -> str:
        return self.__title

    @property 
    def completed(self) -> bool:
        return self.__completed
   
    @completed.setter
    def completed(self, value: bool) -> None:
        self.__completed = value

    @property 
    def instructions_count(self) -> int:
        return self.__instructions_count

    @instructions_count.setter
    def instructions_count(self, value: int) -> None:
        self.__instructions_count = value

    @property 
    def stars_count(self) -> int:
        return self.__stars_count

    def calculate_stars(self, level: Level) -> int:
        
        """
        Calcule et enregistre le nombre d'étoiles obtenues par l'élève
        à la réussite d'un niveau, selon la règle RM-02.

        PRE:
            - Le niveau a été réussi : completed vaut True (RM-08).
            - level est un objet Level avec reference_solution_instructions_count
              entier >= 1 et max_instructions >= reference_solution_instructions_count.
            - instructions_count est un entier compris entre 1 et
              level.max_instructions inclus.

        POST:
            - Retourne 3 si instructions_count <= reference_solution_instructions_count.
            - Retourne 2 si reference_solution_instructions_count < instructions_count
              <= reference_solution_instructions_count + 2.
            - Retourne 1 si instructions_count > reference_solution_instructions_count + 2.
            - stars_count prend la valeur retournée.
            - L'objet level n'est pas modifié.
            - Lève une TypeError si level n'est pas un objet Level ou si
              instructions_count n'est pas un entier, une ValueError si
              completed vaut False ou si instructions_count est hors bornes.
        """
        
        
        if not isinstance(level, Level):
            raise TypeError("level doit être objet de Level") #check if level is an object of Level
        if not isinstance(self.__instructions_count, int):
            raise TypeError("instructions_count doit être un entier") #check if the isntructions_count is an int
        if not self.__completed:
            raise ValueError("Le niveau n'est pas réussi")
        if not 1 <= self.__instructions_count <= level.max_instructions: #check if the number of instructions is between 1 and the max level of isntructions
            raise ValueError("instructions_count est hors borne")
    
        reference  = level.reference_solution_instructions_count 

        if self.__instructions_count <= reference: 
            stars = 3
        elif self.__instructions_count <= reference + 2:
            stars = 2 
        else :
            stars = 1

        self.__stars_count = stars 
        return stars


def report_failure(self, position: Position, level: Level) -> str: #NEED TO BE ADD IN THE CLASS PROGRAM

    """
    Enregistre l'échec de l'essai en cours et construit le message
    explicatif neutre à afficher à l'élève.
    Appelée par run_all() ou run_step_by_step() lorsque le robot
    tente d'aller sur une case refusée par level.is_position_valid().

    PRE:
        - L'objet Program est correctement initialisé.
        - Une exécution est en cours : current_step est l'indice de
          l'instruction en cours, compris entre 0 et len(instructions) - 1.
        - level est un objet Level correctement initialisé.
        - position est un objet Position correspondant à la case que le
          robot a tenté d'atteindre, et level.is_position_valid(position)
          vaut False.

    POST:
        - failed_step prend la valeur current_step + 1 : l'étape est
          numérotée à partir de 1 pour l'élève (EF-04.4).
        - error_message contient le message de l'erreur (EF-04.3) :
            - position hors grille ->
              "Le robot a essayé de sortir de la grille à l'étape {failed_step}."
            - position sur un mur ->
              "Le robot s'est cogné dans un mur à l'étape {failed_step}."
        - Retourne error_message.
        - La liste instructions et la position du robot ne sont pas
          modifiées : l'élève peut corriger son programme et le relancer
          (EF-04.5, EF-04.6).
        - Le message est neutre et ne contient aucun terme culpabilisant
          comme « Perdu » ou « Game over » (ENF-03, ENF-09).
        - Lève une TypeError si position n'est pas un objet Position ou si
          level n'est pas un objet Level, une ValueError si position est
          valide (aucune erreur à signaler).
    """
    
    if not isinstance(level, Level):    #check if level is an object of Level
        raise TypeError("level doit être un objet de Level")
    if not isinstance(position: Position):  #check if position is an object of Position and not a tuple
        raise TypeError("position doit être un objet de Position")
    if level.is_position_valid(position):
        raise ValueError("La position est valide, aucune erreur à signaler") #check if position is valid, if yes nothing happen, if not we raise an error
    
    self.__failed_step = self.__current_step + 1 # +1 because the player start at 1 and we start counting at 0 so his current step is +1

    height = len(level.grid)
    width = len(level.grid[0])

    inside = (0 <= position.row < height and 0 <= position.column < width ) #We put in this var if the cell is in the grid, it returns True or False
                                                                                                 #if both are true, the cell is in the grid
    if not inside:
        self.__error_message = f"Le robot a essayé de sortir de la grille à l'étape {self.__failed_step}." #message if the robot is outside
    else:
        self.__error_message = f"Le robot s'est cogné dans un mur à l'étape {self.__failed_step}." #message if the robot hitted a wall
    return self.__error_message  


def is_position_valid(self, position: Position) -> bool: #NEED TO BE ADD IN THE CLASS LEVEL
    """
    Vérifie si le robot peut se rendre sur la case indiquée par position.

    PRE:
        - L'objet Level est correctement initialisé et sa grille
          est créée et initialisée.
        - self.grid est une liste de lignes non vide, dont chaque ligne
          est une liste de cases (Cell) de même longueur.
        - position est un objet Position dont les attributs row et column
          sont des entiers. Ils peuvent être en dehors des limites de la
          grille : c'est justement ce que la méthode vérifie.

    POST:
        - Retourne False si la position est en dehors de la grille
          (RM-01, EF-04.2) : une position est dans la grille uniquement
          si 0 <= row < height et 0 <= column < width.
        - Retourne False si la cellule contient un mur, de type "wall"
          (RM-06, EF-04.1).
        - Retourne True dans tous les autres cas.
        - La grille et le niveau ne sont pas modifiés.
        - Lève une TypeError si position n'est pas un objet Position ou si
          row / column ne sont pas des entiers.
    """
    
    if not isinstance(positon, Position): #check if position is an object of Position and not a tuple
        raise TypeError("position doit être un objet de Position")
    if not isinstance(position.row, int) or not isinstance(position.column, int): #check if the number of column or row is an int
        raise TypeError("row et column doivent être des entiers")

    height = len(self.grid)
    width = len(self.grid[0])


    if not (0 <= position.row < height and 0 <= position.column < width): #(self because method is in level) not because we want to know if the cell IS NOT in the grid
        return False 
    
    cell = self.grid[position.row][position.column]
    if cell.type_cell == "wall":
        return False
    else:
        return True #check if the cell is a wall, it returns False if it is. So the robot cant go there
    

def reset(self) -> None: #NEED TO BE ADD IN THE CLASS PROGRAMM
    """reset the level"""
    
    self.__current_step = 0
    self.__failed_step = None
    self.__error_message = ""
    self.__robot.current_position = self.__level.start_position
    self.__robot.direction = "up"
    self.__robot.collected_gems = 0 #voir si hongkun a le même setter, il en a pas donc je suppose qu'on peut mettre ça