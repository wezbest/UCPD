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
# -------------------------------------------------------


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
