#!/usr/bin/env python3.12

'''
Testing module system here
'''
# beautifiers
# Beauty Panty

# ------------------------------------------------------
import utility as u
import bussy.lickk as lq
import sho.sho as sho
import studa.rando as rando
import sys
# -------------------------------------------------------c

# Importing the utility.py in the same folder
lq.inspect(u)

lq.rprint(lq.Panel("Simple utility import - importing utility.py", box=lq.box.ROUNDED,
                   expand=False,  border_style="magenta"))

lq.rprint(f"""
Multiplication: {u.multi(10, 20)}
Division: {u.divi(10, 20)}
""")

lq.rprint(lq.Panel("Importing sho.py from sho", box=lq.box.ROUNDED,
                   expand=False,  border_style="magenta"))

lq.pprint(sho.buyy("Laptop"))

lq.rprint(lq.Panel("Exeute studa/rando.py", box=lq.box.ROUNDED,
                   expand=False,  border_style="magenta"))

# lq.rprint(list(rando.randoz()))
lq.rprint(list(rando.randoz()))

lq.rprint("Printin random number between 0 to 1 - iteration 10")
lq.rprint(list(rando.randoz2()))

lq.rprint("Choice - iteration 10")
lq.rprint(list(rando.rando_choice()))

lq.rprint("Shuffler - iteration 10")
lq.rprint(rando.rando_shuff())

# This section is for he sys package
