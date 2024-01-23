'''
Testing out classes and instantiation 
'''

# Beautifiers
import filez.f1 as f1
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()


def ex122():
    """
    Excercise 122
    """
    console.print(Panel("Excercise 122 - Solution", border_style="red"))
    f1.f11()
    # Given class

    class Cat:
        species = 'mammal'

        def __init__(self, name, age):
            self.name = name
            self.age = age

    # Instantiate Cat object with 3 cats
    cat1 = Cat("Tom", 3)
    cat2 = Cat("Garfield", 5)
    cat3 = Cat("Whiskers", 2)

    # Function to find the oldest cat
    def oldest_cat(*args):
        return max(args)

    # Print out the oldest cat
    rprint(oldest_cat(cat1.age, cat2.age, cat3.age))

    Oldest_Cat = oldest_cat(cat1.age, cat2.age, cat3.age)
    rprint(f"The oldest cat is {Oldest_Cat}")
