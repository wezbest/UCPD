#!/usr/bin/env python3.12
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()
# Create a Text object with centered text for the Panel
text = Text("Centered Text in a Panel", style="bold", justify="right")
# Create a Panel with the Text object
panel = Panel(text)
# Print the Panel
console.print(panel)