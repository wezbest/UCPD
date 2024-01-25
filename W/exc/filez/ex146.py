'''
Excercise 146 - Map Reduce filtering
'''

#  Beautifiers
# ------------------------------------------------------
from rich import print as rprint  # For rprinting
from rich.pretty import pprint  # For pretty printing
from rich import inspect  # For inspect
from rich.console import Console  # For console.print
from rich.markdown import Markdown  # For markdown
from rich.panel import Panel  # For Panel()
from rich import box  # For Panel Boxes
from rich.prompt import Prompt  # For Prompting
console = Console()  # Standard code to access console
# -------------------------------------------------------


def ex146():
    rprint(Panel('Excercise 146 - Map Reduce filtering', title="My Exc"))

    # Capitalize this list
    my_pets = ['sisi', 'bibi', 'titi', 'carla']

    def capitilize(str):
        return str.capitalize()

    new_pets = list(map(capitilize, my_pets))
    console.print("Capitalize my pets : ",  style="blue")
    rprint(new_pets)

    # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [5, 4, 3, 2, 1]

    def zip_func(string, number):
        return string, number
    console.print("\n\n Zip combining lists",  style="blue")
    rprint(list(zip(my_strings, sorted(my_numbers))))

    # 3 Filter the scores that pass over 50%
    scores = [73, 20, 65, 19, 76, 100, 88]

    def filter_func(score):
        return score > 50
    console.print("\n\n Filter scores",  style="blue")
    rprint(list(filter(filter_func, scores)))
