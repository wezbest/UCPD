#!/usr/bin/env python3.12

from rich.console import Console
from rich.text import Text

console = Console()

# Create a Text object with the content you want to center-align
text = Text("Centered Text", style="bold")

# Use the console to print the text, center-aligned
console.print(text, justify="center")