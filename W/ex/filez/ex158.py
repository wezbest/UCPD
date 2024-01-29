'''
Excercise 158 
'''

# Prettifiers
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()


def ex158():
    """
    Excercise 158 - 
    """
    console.print(Panel("Excercise 158 - Decorators", border_style="red"))

    user1 = {
        'name': 'Sorna',
        # changing this will either run or not run the message_friends function.
        'valid': False
    }

    def authenticated(fn):
        def wrapper(*args, **kwargs):
            if user1['valid']:
                return fn(*args, **kwargs)
            else:
                rprint(user1)
                console.print("[red blink]DIE BASTARD !!!")
        return wrapper

    @authenticated
    def message_friends(user1):
        rprint(user1)
        print("message has been sent")

    message_friends(user1)
