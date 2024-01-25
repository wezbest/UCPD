'''
Ex 151 - Using list comprehensions 
'''

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


def ex151():
    """
    Solution for ex 151
    """
    console.print(
        Panel("""Chapter 151 - Solution - List and Set comprehensions.""", border_style="red"))

    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    console.print('\n [blue]Finding duplicates using list comprehension')
    duplicates = [x for x in some_list if some_list.count(x) > 1]
    dumplicates2 = {x for x in some_list if some_list.count(x) > 1}
    rprint(f'Duplicate elements in {some_list} are : ', duplicates)
    rprint(f'Duplicate elements in {some_list} using set comprehension are : ', dumplicates2)
    



