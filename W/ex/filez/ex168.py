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
    console.print(
        Panel("Excercise 168 - Finonacci Numbers", border_style="magenta"))

    # write a function to generate fibonacci sequence without using python functions 
    
    # def fib(n):
    #     a,b = 0,1 
    #     for i in range(n):
    #         yield a
    #         a,b = b,a+b
    # for i in fib(20):
    #     rprint(i)

    #doing the same with a list - this given a nice list response
    def fib2(n):
        a,b = 0,1
        result = []
        for i in range(n):
            result.append(a)
            a,b = b,a+b
        return result
    rprint(fib2(20))

    # def fib(n):
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return fib(n-1) + fib(n-2)
    
    # # Call function 
    # rprint(fib(30))
