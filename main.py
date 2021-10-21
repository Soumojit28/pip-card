from rich.console import Console
from rich import box
from rich.align import Align
from rich.table import Table
from rich.text import Text

console = Console()

table = Table(title="Hey Folks!", show_header=False)

console.print("Hello", "World!", style="bold red", justify="center")



# table.add_column(justify="center", style="cyan")
# table.add_column(justify="left", style="magenta")


# table_centered = Align.center(table)
# # console.print(table_centered)