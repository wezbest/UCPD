'''
Rich imports for calling in all excercise files
'''

# Rich Impports
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()

# Heading Panel here
panel = Panel("""
Enjoy StinlySmellySWeaty women
""", title="Mistress", subtitle="ToiletSlave", style="Italic", border_style="magenta")
# Print the Panel
console.print(panel)

console.print("""
              Centered Text - mistress fart
              in mouth and nose
              """, style="bold", justify="center")
