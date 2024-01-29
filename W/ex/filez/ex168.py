'''
Excercise 168 - Write python function for fibonacci numbers
'''

# Prettifiers
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()


def ex168():
    """
    Excercise 158 - 
    """
    console.print(Panel("Excercise 168 - Finonacci Numbers", border_style="magenta"))

    # write a function to generate fibonacci sequence 
    fibo = [0, 1]
    for i in range(2, 10):
        fibo.append(fibo[i-1] + fibo[i-2])
        print(fibo[i])