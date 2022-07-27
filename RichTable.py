from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Account", justify="right")
table.add_column("Username", justify="right")
table.add_row(
    "Dec 09, 2021", 
    "YouTube", 
    "KAZEDEVID", 
    "Kaze"
)
table.add_row(
    "May 25, 2021",
    "Instagram",
    "@lordagam23_",
    "Kaze",
)
table.add_row(
    "Feb 15, 2022",
    "Tiktok",
    "@punyakaze91",
    "Kaze 91",
)
table.add_row(
    "Sep 21, 2021",
    "Snack Video",
    "kuira360",
    "Lord Kaze🗿",
)

console.print(table)