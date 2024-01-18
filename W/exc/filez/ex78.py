'''
78: First GUI
'''

# Prettification
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Write main function here which will be imported

def ex78():
    """_summary_
    Function for the excercise which will be called in main
    """

    # Where there is 1 replace it with * and where there is 0 replace it with space

    picture = [
      [0,0,0,1,0,0,0],
      [0,0,1,1,1,0,0],
      [0,1,1,1,1,1,0],
      [1,1,1,1,1,1,1],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]
    ]
    '''
    Here the picture is atually composed of many lists
    and you will search it as row and lists and add the end"" 
    to print the picture
    '''
    for row in picture:
        for col in row:
            if col == 1:
                rprint([green]"*", end="")
            else:
                rprint(" ", end="")
        rprint()