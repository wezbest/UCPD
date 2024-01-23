#!/usr/bin/env python3.12

'''
Testing the requests package here
'''

# Beautifiers
# ---------------------------------------------------------------
# Beautifers
import requests as r
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()
# ---------------------------------------------------------------

rprint(Panel('Printing pix/s1.ansi', box=box.ROUNDED,
       title='ANSI', title_align='center'))

url = 'https://snips.sh/f/Tv2OQSoagn?r=1'

response = r.get(url)
print(response.text)
