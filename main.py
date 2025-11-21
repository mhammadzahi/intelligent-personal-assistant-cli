import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from database import init_db
from controllers import TaskController, NoteController, ReminderController
from notifications import check_reminders
from utils import parse_date, format_date

console = Console()

def list_tasks(args):
    tasks = TaskController.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="Tasks")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Category", style="green")
    table.add_column("Status", style="blue")

    for task in tasks:
        status_style = "strike" if task.status == "done" else ""
        table.add_row(str(task.id), task.title, task.category, task.status, style=status_style)

    console.print(table)

def add_task(args):
    task = TaskController.add_task(args.title, args.category)
    console.print(f"[bold green]Task added:[/bold green] {task.title} (ID: {task.id})")

def delete_task(args):
    TaskController.delete_task(args.id)
    console.print(f"[bold red]Task deleted:[/bold red] ID {args.id}")

def complete_task(args):
    TaskController.update_status(args.id, "done")
    console.print(f"[bold green]Task marked as done:[/bold green] ID {args.id}")

def list_notes(args):
    notes = NoteController.get_all_notes()
    if not notes:
        console.print("[yellow]No notes found.[/yellow]")
        return

    table = Table(title="Notes")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Summary", style="green")

    for note in notes:
        table.add_row(str(note.id), note.title, note.summary)

    console.print(table)

def add_note(args):
    console.print("[dim]Generating summary...[/dim]")
    note = NoteController.add_note(args.title, args.content)
    console.print(f"[bold green]Note added:[/bold green] {note.title} (ID: {note.id})")
    console.print(Panel(note.summary, title="Summary", expand=False))

def delete_note(args):
    NoteController.delete_note(args.id)
    console.print(f"[bold red]Note deleted:[/bold red] ID {args.id}")

def search_notes(args):
    notes = NoteController.search_notes(args.query)
    if not notes:
        console.print("[yellow]No matching notes found.[/yellow]")
        return
        
    table = Table(title=f"Search Results: '{args.query}'")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Summary", style="green")

    for note in notes:
        table.add_row(str(note.id), note.title, note.summary)

    console.print(table)

def list_reminders(args):
    reminders = ReminderController.get_all_reminders()
    if not reminders:
        console.print("[yellow]No reminders found.[/yellow]")
        return

    table = Table(title="Reminders")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Due Date", style="red")

    for reminder in reminders:
        table.add_row(str(reminder.id), reminder.title, reminder.due_date)

    console.print(table)

def add_reminder(args):
    try:
        # Validate date format
        parse_date(args.date)
        reminder = ReminderController.add_reminder(args.title, args.date)
        console.print(f"[bold green]Reminder set:[/bold green] {reminder.title} for {reminder.due_date}")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def delete_reminder(args):
    ReminderController.delete_reminder(args.id)
    console.print(f"[bold red]Reminder deleted:[/bold red] ID {args.id}")

def main():
    init_db()
    check_reminders()

    parser = argparse.ArgumentParser(description="Intelligent Personal Assistant")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Task commands
    task_parser = subparsers.add_parser("task", help="Manage tasks")
    task_subparsers = task_parser.add_subparsers(dest="subcommand")

    task_add = task_subparsers.add_parser("add", help="Add a task")
    task_add.add_argument("title", help="Task title")
    task_add.add_argument("--category", default="general", help="Task category")
    task_add.set_defaults(func=add_task)

    task_list = task_subparsers.add_parser("list", help="List tasks")
    task_list.set_defaults(func=list_tasks)

    task_del = task_subparsers.add_parser("delete", help="Delete a task")
    task_del.add_argument("id", type=int, help="Task ID")
    task_del.set_defaults(func=delete_task)

    task_done = task_subparsers.add_parser("done", help="Mark task as done")
    task_done.add_argument("id", type=int, help="Task ID")
    task_done.set_defaults(func=complete_task)

    # Note commands
    note_parser = subparsers.add_parser("note", help="Manage notes")
    note_subparsers = note_parser.add_subparsers(dest="subcommand")

    note_add = note_subparsers.add_parser("add", help="Add a note")
    note_add.add_argument("title", help="Note title")
    note_add.add_argument("content", help="Note content")
    note_add.set_defaults(func=add_note)

    note_list = note_subparsers.add_parser("list", help="List notes")
    note_list.set_defaults(func=list_notes)

    note_del = note_subparsers.add_parser("delete", help="Delete a note")
    note_del.add_argument("id", type=int, help="Note ID")
    note_del.set_defaults(func=delete_note)

    note_search = note_subparsers.add_parser("search", help="Search notes")
    note_search.add_argument("query", help="Search query")
    note_search.set_defaults(func=search_notes)

    # Reminder commands
    reminder_parser = subparsers.add_parser("reminder", help="Manage reminders")
    reminder_subparsers = reminder_parser.add_subparsers(dest="subcommand")

    reminder_add = reminder_subparsers.add_parser("add", help="Add a reminder")
    reminder_add.add_argument("title", help="Reminder title")
    reminder_add.add_argument("date", help="Due date (YYYY-MM-DD HH:MM)")
    reminder_add.set_defaults(func=add_reminder)

    reminder_list = reminder_subparsers.add_parser("list", help="List reminders")
    reminder_list.set_defaults(func=list_reminders)

    reminder_del = reminder_subparsers.add_parser("delete", help="Delete a reminder")
    reminder_del.add_argument("id", type=int, help="Reminder ID")
    reminder_del.set_defaults(func=delete_reminder)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
