from rich.console import Console
from rich.table import Table

from utils import load_rich_table_config
from utils import create_rich_table

if __name__ == "__main__":
    console = Console()

    table_config = load_rich_table_config()
    table = create_rich_table(table_config)

    table.add_column(header="Test Header1")
    table.add_column(header="Test Header2")
    
    table.add_row("test data11", "test data12")
    table.add_row("test data21", "test data22")
    
    console.print(table)
