from controllers import ReminderController
from rich.console import Console
from rich.panel import Panel

console = Console()

def check_reminders():
    """Checks for due reminders and displays them."""
    due_reminders = ReminderController.get_due_reminders()
    if due_reminders:
        for reminder in due_reminders:
            console.print(Panel(f"[bold red]REMINDER DUE:[/bold red] {reminder.title}\n[dim]Due: {reminder.due_date}[/dim]", title="🔔 Notification", expand=False))
            # Mark as done or notified? For now, just leave as pending or maybe we should have a 'notified' status?
            # The requirement says "Console notifications for upcoming reminders".
            # Let's not auto-complete them, but maybe we should avoid spamming.
            # For this simple CLI, checking on run is fine.
