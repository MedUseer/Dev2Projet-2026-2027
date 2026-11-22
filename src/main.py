import threading as th
import model.Level as m
import controller.level_controller as c
import view.GameInterface as v


def create_thread(reference_function,param1,param2) -> None:
    """
    """
    th.Thread(target=reference_function,args=[param1,param2],daemon=True).start()


print("Bienvenu sur la création d'un niveau :) \n")
interface = v.GameInterface() # create a object view
interface.window.geometry("600x800")# define the window size
level = m.Level() # create a level object

create_thread(c.create_level,interface,level)

interface.window.mainloop() # start the window
