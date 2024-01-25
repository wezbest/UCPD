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
    rprint(Panel('Excercise 78 - using neste4d for loops for printing image', title="My Exc"))
    # Where there is 1 replace it with * and where there is 0 replace it with space

    picture = [
        [0, 0, 0, 1, 0, 0, 0],  # Each one of this is s row
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    '''
    Here the picture is atually composed of many lists
    and you will search it as row and lists and add the end"" 
    to print the picture
    '''
    fill = '*'
    empty = '_'
    i = 0
    while True:
        for row in picture:  # reading it line by line row
            for col in row:  # then search through each column
                if col == 1:
                    rprint(f"[green]{fill}[/green]", end="")
                else:
                    rprint(f"[red]{empty} ", end="")
            rprint()
        i += 1
        if i >= 2:
            break
