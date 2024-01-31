#!/usr/bin/env python3.12
'''
Testing the choices function 
'''
# ------------------------------------------------------
import random
import lickk as lq


choices = [1, 2, 3]
while True:
    choices_shuffle = random.choice(choices)
    lq.rprint(
        f"[yellow bold]Debug - Shuffled Number {choices_shuffle}[/yellow bold]")
    user_choice = int(input("Enter Number of panty:"))

    if (user_choice == choices_shuffle):
        lq.console.print(lq.Panel(f"""Mistress will fart in your face - 
You chose {user_choice} 
and winner is {choices_shuffle}""", expand=False))
        break
    else:
        lq.console.print(f"[red] FUCKED !!! [/red]You Chose {user_choice}")
