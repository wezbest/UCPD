#!/usr/bin/env python3.12

'''
Testing module system here
'''
# beautifiers
# Beauty Panty

# ------------------------------------------------------
import utility
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


# Importing the utility.py in the same folder
inspect(utility, all=True)