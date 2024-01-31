#!/usr/bin/env python3.12
'''
syg.py - Doing assignmen 
- Write a sysrgv python file that accepts arguments using random choice
'''

import lickk as lq
import random
import sys

# Sample code
'''
first = sys.argv[1]
second = sys.argv[2]
lq.rprint(f"First: {first}, Second: {second}")
'''

choices = random.randint(1,5)
randmized_choice = random.choice(choices)
lq.rprint(f"Random Choice: {randmized_choice}")
user_input = int(sys.argv[1])
if (user_input == randmized_choice):
    lq.console.print(lq.Panel(f"""[green]Winner
                              Your Choice {user_input}
                              Random Choice {randmized_choice}
                              [/green]""", expand=False, title="Winner", border_style="green"))
else:
    lq.console.print(lq.Panel(f"""[red]Loser
                              Your Choice {user_input}
                              Random Choice {randmized_choice}
                              [red]""", expand=False, title="Loser", border_style="red"
                              ))
