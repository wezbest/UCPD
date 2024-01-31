'''
Testing the choices function 
'''
import bussy.lickk as lq
import random

choices = [1, 2, 3]
while True:
    choices_shuffle = random.choice(choices)
    lq.rprint(f"Debug - Shuffled Number {choices_shuffle}")
    user_choice = int(input("Enter Number of panty:"))
    if (user_choice == choices_shuffle):
        lq.console.print(lq.Panel(f"""Mistress will fart in your face - 
        You chose {user_choice} and winner is {choices_shuffle}"""))
        break
    else:
        lq.console.print(f"[red] FUCKED !!! [/red]You Chose {user_choice}")
