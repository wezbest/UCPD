'''
Execercise 90 : Solution is here
'''

#  Beautification
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Code logic here 
# Create functio highest function , which takes alist as an argument

# call main file function 
def e90():
    def highest_even(li):
        evens = []
        for i in li:
            if i % 2 == 0:
                evens.append(i)
        return max(evens)