"""Command-line interface for the task manager."""

import click
from rich.console import Console
from rich.table import Table

from src.models.task import TaskStatus
from src.services.task_manager import TaskManager

console = Console()
manager = TaskManager()


@click.group()
def cli():
    """Task Manager CLI - Manage your tasks from the command line."""
    pass


@cli.command()
@click.argument("title")
@click.argument("description")
def add(title: str, description: str):
    """Add a new task.

    Example: python -m src.cli.main add "Learn Python" "Complete workshop"
    """
    task = manager.add_task(title, description)
    console.print(f"[green]✓[/green] Task created: {task.title} (ID: {task.id})")


@cli.command()
@click.option(
    "--status",
    type=click.Choice(["todo", "in_progress", "done"]),
    help="Filter by status",
)
def list(status: str | None):
    """List all tasks.

    Example: python -m src.cli.main list
    Example: python -m src.cli.main list --status todo
    """
    # Convert string to enum if status provided
    status_filter = TaskStatus(status) if status else None
    tasks = manager.list_tasks(status=status_filter)

    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    # Create a beautiful table
    table = Table(title="Tasks", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan", width=6)
    table.add_column("Title", style="white")
    table.add_column("Status", style="green")
    table.add_column("Created", style="dim")

    for task in tasks:
        # Color status based on value
        status_color = {
            TaskStatus.TODO: "[yellow]📌 TODO[/yellow]",
            TaskStatus.IN_PROGRESS: "[blue]🚧 IN PROGRESS[/blue]",
            TaskStatus.DONE: "[green]✓ DONE[/green]",
        }

        table.add_row(
            str(task.id),
            task.title,
            status_color[task.status],
            task.created_at.strftime("%Y-%m-%d %H:%M"),
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(tasks)} task(s)[/dim]")


@cli.command()
@click.argument("task_id", type=int)
@click.argument(
    "status",
    type=click.Choice(["todo", "in_progress", "done"]),
)
def update(task_id: int, status: str):
    """Update task status.

    Example: python -m src.cli.main update 1 done
    """
    status_enum = TaskStatus(status)
    task = manager.update_task_status(task_id, status_enum)

    if task is None:
        console.print(f"[red]✗[/red] Task {task_id} not found")
        return

    console.print(f"[green]✓[/green] Task {task_id} updated to {status}")


@cli.command()
@click.argument("task_id", type=int)
@click.confirmation_option(prompt="Are you sure you want to delete this task?")
def delete(task_id: int):
    """Delete a task.

    Example: python -m src.cli.main delete 1
    """
    success = manager.delete_task(task_id)

    if not success:
        console.print(f"[red]✗[/red] Task {task_id} not found")
        return

    console.print(f"[green]✓[/green] Task {task_id} deleted")


@cli.command()
def stats():
    """Display task statistics.

    Example: python -m src.cli.main stats
    """
    total = manager.count_tasks()
    todo = manager.count_by_status(TaskStatus.TODO)
    in_progress = manager.count_by_status(TaskStatus.IN_PROGRESS)
    done = manager.count_by_status(TaskStatus.DONE)

    console.print("\n[bold]📊 Task Statistics[/bold]\n")
    console.print(f"  Total tasks: [cyan]{total}[/cyan]")
    console.print(f"  📌 TODO: [yellow]{todo}[/yellow]")
    console.print(f"  🚧 IN PROGRESS: [blue]{in_progress}[/blue]")
    console.print(f"  ✓ DONE: [green]{done}[/green]")

    if total > 0:
        completion = (done / total) * 100
        console.print(f"\n  Completion: [green]{completion:.1f}%[/green]\n")


if __name__ == "__main__":
    cli()
