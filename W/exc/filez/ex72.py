'''
Excercise - Chapter 72 
'''

# Beautification 
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Writing the function here
def e72():
    """
    Solution for ex 72
    """
    console.print(Panel("""Chapter 72 - Solution- Making a tricky counter""", border_style="red"))
    
    my_counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rprint("Counter Pussies")
    counter = 0
    for item in my_counter:
        counter += item
    rprint("Sum of all the numers is :" ,counter)
