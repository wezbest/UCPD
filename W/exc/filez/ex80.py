'''
Chapter 80 - Finding duplicates
'''

# Beautification 
# Adding these for rich input
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Define function 

def ex80():
    """
    Solution for ex 80
    """
    console.print(Panel("""Chapter 80 - Solution- Finding duplicates""", border_style="red"))
    
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    rprint(f'Duplicate elements in {some_list} are : ',duplicates)