#!/usr/bin/env python3.12

# Importing the prettification
# Adding these for rich input
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
console = Console()

# Actual Coding will start here 

# This is the example given
is_old = True
is_lic = True 

titt = """
# Conditionals 
> This for writing various conditionals 

## Using

```py
# Writinbg Python
if someshit :
```

"""
tit_md = Markdown(titt)
console.print(tit_md)

rprint(Panel("Hello, [red]World!", box=box.ASCII))

if is_old: 
    rprint('CheckID')
console.print('NO WAY')