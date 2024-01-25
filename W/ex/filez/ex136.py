'''
Solution for ex136
'''

# Beauifier s
import filez.pu as p1
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Writing the main function here


def ex136():
    p1.run_fetch_snips_pussy()
    rprint(Panel('Excercise 132 - Classes', title="My Exc"))
    
    # Actual code will go here
    '''
    In this solution the Superlist class is inheriting the functionsality 
    of a list, and u are then creating an instance of SuperList, this is example
    of how to extend the list class to inherit the functionailty of a list
    '''
    class SuperList(list):
        
        def __len__(self):
            return 1000
        
    super_list1 = SuperList()
    super_list1.append(5)
    rprint(len(super_list1))
    rprint(super_list1[0])
    
    # Checking if SuperList is subclass of list
    rprint(issubclass(SuperList, list))