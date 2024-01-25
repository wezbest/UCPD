'''
Code for excercise 132
'''

# Add beautifiers
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


def ex132():
    p1.run_fetch_snips_pussy()
    rprint(Panel('Excercise 132 - Classes', title="My Exc"))

    # This class will be used for the pet actions
    class Pets():
        animals = []

        def __init__(self, animals):
            self.animals = animals

        def walk(self):
            for animal in self.animals:
                print(animal.walk())

        # Adding a singing section here
        def sing(self):
            for animal in self.animals:
                rprint(animal.sing('eee'))

    # Class is for defining cat class 
    class Cat():
        is_lazy = True

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def walk(self):
            return f'{self.name} is just walking around'

    # Instantiating the classes here
    class Simon(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Sally(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    # adding another
    class Pussy(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    # Create a list of all of the pets (create 3 cat instances from the above)
    # Create 3 cat instances
    simon = Simon("Simon", 4)
    sally = Sally("Sally", 5)
    pussy = Pussy("Pussy", 3)

    # Add the cat instances to the pets list
    my_cats = [simon, sally, pussy]

    # Instantiate the Pets class with all your cats using the variable my_cats
    pets = Pets(my_cats)

    # Output all of the cats walking using the my_pets instance
    console.print('\n [green] Walking around all pets \n')
    pets.walk()
    console.print('\n [magenta] Singing here \n')
    pets.sing()