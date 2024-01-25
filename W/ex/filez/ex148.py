'''
Exercise 148 - Lambda Expressions excercise 
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

def ex148():
    """
    Solution for ex 148
    """
    console.print(Panel("""Chapter 148 - Solution- Lambda Expressions""", border_style="red"))
    
    # Writing a square function 
    li = list(range(1,10))
    console.print("Square of list items:", list(map(lambda x : x**2, li)))
    
    # Using lambda expression sort list  tuples 
    a = [(0, 2), (4, 3), (10, -1), (9, 9)]
    a.sort(key=lambda x: x[1])
    console.print("oringinal list:", a)
    console.print("Sorted list:", a)
    
    
