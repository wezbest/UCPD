#!/usr/bin/env python3.12
'''
Testing the choices function 
'''
# ------------------------------------------------------
import random
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



choices = [1, 2, 3]
while True:
    choices_shuffle = random.choice(choices)
    rprint(f"Debug - Shuffled Number {choices_shuffle}")
    user_choice = int(input("Enter Number of panty:"))
    if (user_choice == choices_shuffle):
        console.print(Panel(f"""Mistress will fart in your face - 
You chose {user_choice} 
and winner is {choices_shuffle}"""))
        break
    else:
        console.print(f"[red] FUCKED !!! [/red]You Chose {user_choice}")
