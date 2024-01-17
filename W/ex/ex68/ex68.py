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
console = Console()

# Actual Solution 
is_magician = True
is_expert = True

# Check if magician and expert: "you are a master magician"
rprint(Panel.fit('Ex1'))
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
rprint(Panel.fit('Ex2'))
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
rprint(Panel.fit('Ex3'))
is_magician3 = False
is_expert3 = True
if not is_magician3:
    rprint(f"""
    Variables
    is_magician3  = {is_magician3}
    is_expert3    = {is_expert3}
    """)
    rprint("You need magic powers")