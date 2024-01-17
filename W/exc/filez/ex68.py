#!/usr/bin/env python3.12

'''
Ex68 - from UTCPC
'''

# Beautifcation 
# Adding these for rich input
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

def ex68():
    """
    Excercise 68 as a funbction
    """
# Actual Solution 
    is_magician = True
    is_expert = True

    # Check if magician and expert: "you are a master magician"
    console.print(Panel('Ex1'))
    is_magician = True
    is_expert = True
    rprint(f"""
        Variables
        is_magician  = {is_magician}
        is_expert    = {is_expert}
        """)
    if is_magician and is_expert:
        rprint("You are a master magician")

    # Check if magician but not expert: "at least you're getting there"
    console.print(Panel('Ex2'))
    is_magician2 = True
    is_expert2 = False

    if is_magician2 and not is_expert2:
        rprint(f"""
        Variables
        is_magician2  = {is_magician2}
        is_expert2    = {is_expert2}
        """)
        rprint("At least you're getting there")

    # Check if not a magician: "You need magic powers"
    console.print(Panel('Ex3'))
    is_magician3 = False
    is_expert3 = True
    if not is_magician3:
        rprint(f"""
        Variables
        is_magician3  = {is_magician3}
        is_expert3    = {is_expert3}
        """)
        rprint("You need magic powers")


    # Alternative method 
    is_m1 = Prompt.ask("R U bastard Magician? :", default=("N"), choices=['Y', 'N'])
    is_e1 = Prompt.ask("R U an Pussy Licking Expert :", default=("N"), choices=['Y', 'N'])

    is_mag = True
    is_exp = True

    # Writing all the 3 conditions here 
    console.print(Panel('My Sol'))
    rprint(f"""
           Choices 
           is_m1 = {is_m1}
           is_e1 = {is_e1}
           """)
    if is_m1=="Y" and is_e1=="Y":
        console.print("[green]You are a master Faggot magician[/green]")
    elif is_m1=="Y" and is_e1=="N":
        console.print("[yellow]At least you're getting there[/yellow]")
    elif is_m1=="N" and is_e1=="N":
        console.print("[red]You need magic powers,DIE BASTARD ![/red]")
