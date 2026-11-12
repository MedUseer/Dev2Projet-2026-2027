dico_direction = {}

class Program:
    def __init__(self, instruction: list, failed_step:int, current_step:int, error_message:str):
        
        pass
    
    def count_instruction(self) -> int:
        
        pass
    
    def run_all(self) -> bool:
        
        pass
    
    def run_step_by_step(self) -> bool:
        
        pass
    
    def reached(self) -> bool:
        
        pass

class Robot:
    def __init__(self, current_position, direction : dico_direction):
        self.current_position = current_position
        self.direction = direction
    
    def move_forward(self):
        
        pass

    def move_left(self):
        
        pass

    def turn_right(self):
        
        pass

    def collect_gems(self, type_cells: dico_type_cells = "empty"):
        
        pass