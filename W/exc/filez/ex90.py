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
    rprint(Panel('Excercise 90 - Find the highest even number in a list', title="My Exc"))

    rprint(highest_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
