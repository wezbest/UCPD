#!/usr/bin/env python3.12

from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

pretty = Pretty(locals())
panel = Panel(pretty)
print(panel)