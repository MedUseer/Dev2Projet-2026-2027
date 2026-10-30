import emoji # import the emoji library for display.

dico_type_cells = {
        "gem": "\033[32m▪\033[0m", # code ANSI
        "wall" : emoji.emojize(":rock:"),
        "robot" : emoji.emojize(":robot:"),
        "arrival":emoji.emojize(":round_pushpin:"),
        "empty":"_"
}

"""
MEMO tech - type of cells

- 📍 --> symbol for arrival

- 🪨 -> symbol for wall

- 🤖 -> symbole for start/robot

- ▪ (green)-> symbol for gem


design example for grid
|_| |_| |_|
|_| |_| |_|
|_| |_| |_|

gem - > U+1F7E9 code unicode


"""
# MVP - version 1

class Position:

    def __init__(self,row : int,column : int):
        self.row = row
        self.column = column

    #methods
    
    def get_row(self):
        """
            doc soon ...
        """
        return self.row
    
    def get_column(self):
        """
            doc soon ...
        """
        return self.column


class Cell:
    
    def __init__(self,position : Position,type="empty"):
        self.position = position
        self.type = type

    #methods
    def get_type(self):
        """
            doc soon ...
        """
        return self.type
