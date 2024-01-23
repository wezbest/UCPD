#!/usr/bin/env python3.12

'''
Making the t1.py , into an async request
'''

# Beautifiers
# ---------------------------------------------------------------
# Beautifers
import requests as r
import asyncio
import aiohttp
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

# ------------------------------------------------------
# Working requests code below changed to async

# rprint(Panel('Printing pix/s1.ansi', box=box.ROUNDED,
#        title='ANSI', title_align='center'))

# url = 'https://snips.sh/f/Tv2OQSoagn?r=1'

# response = r.get(url)
# print(response.text)
# ---------------------------------------------------

# Making following function async with asynchio and aiohttp


async def fetch_pastebin():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://snips.sh/f/Tv2OQSoagn?r=1') as response:
            print(await response.text())
            rprint(Panel('Sniff her'))


# write a loop to call the function
for _ in range(3):
    asyncio.run(fetch_pastebin())
