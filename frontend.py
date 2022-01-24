import evaluate
import sys
import rich
from rich.console import Console

console = Console()
repl_code = evaluate.run(sys.argv[1])

if repl_code == 1:
    console.log("python [green]SUCCESS[/]")
elif isinstance(repl_code, evaluate.PyException):
    console.log(f"python [red]ERROR:[/]\n{repl_code.info[0]}:{repl_code.info[1]}")
else:
    console.log(f"pydbug [red]FATAL:[/]\nUnknown Error Code '{repl_code}'")
